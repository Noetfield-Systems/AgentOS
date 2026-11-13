"""Negative-path and replay tests for the official Paperclip Issue API adapter."""
import importlib.util
import io
import json
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

SCRIPT = (Path(__file__).resolve().parents[1] / "integrations" / "paperclip"
          / "authorized_issue_bridge.py")
spec = importlib.util.spec_from_file_location("paperclip_bridge", SCRIPT)
bridge = importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name] = bridge
spec.loader.exec_module(bridge)


class Response:
    def __init__(self, value):
        self.reader = io.BytesIO(json.dumps(value).encode())
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc, tb):
        self.reader.close()
    def read(self, size):
        return self.reader.read(size)


class PaperclipBridgeTests(unittest.TestCase):
    def setUp(self):
        self.calls = []
        self.created_ids = ["task-123"]

    def packet(self, **changes):
        data = {
            "company_id": "company-123",
            "project_id": "project-123",
            "workpacket_id": "wp-123",
            "title": "Ship one verified feature",
            "description": "Create a versioned artifact and test it",
            "goal_digest": "a" * 64,
            "expires_at": (datetime.now(timezone.utc) +
                           timedelta(minutes=30)).isoformat(),
        }
        data.update(changes)
        return bridge.WorkPacket(**data)

    def transport(self, request, timeout):
        self.calls.append(request)
        self.assertEqual(timeout, 8.0)
        self.assertEqual(request.get_header("Authorization"), "Bearer " + "x" * 40)
        if request.get_method() == "POST":
            body = json.loads(request.data.decode())
            self.assertEqual(body["projectId"], "project-123")
            self.assertEqual(body["status"], "todo")
            self.assertIn("idempotencyKey", body)
            self.assertNotIn("permit", body)
            return Response({"id": "task-123"})
        return Response({
            "id": "task-123", "companyId": "company-123",
            "projectId": "project-123"
        })

    def client(self, admit=None):
        return bridge.PaperclipAPI(
            "https://paperclip.example.test",
            "x" * 40, admit=admit, transport=self.transport
        )

    def test_missing_authority_never_calls_paperclip(self):
        with self.assertRaises(bridge.AdmissionDenied):
            self.client().create_authorized_issue(self.packet())
        self.assertFalse(self.calls)

    def test_denied_authority_never_calls_paperclip(self):
        with self.assertRaises(bridge.AdmissionDenied):
            self.client(admit=lambda p: False).create_authorized_issue(self.packet())
        self.assertFalse(self.calls)

    def test_expired_workpacket_rejected(self):
        p = self.packet(expires_at=(datetime.now(timezone.utc) -
                                    timedelta(seconds=10)).isoformat())
        with self.assertRaises(bridge.AdmissionDenied):
            self.client(admit=lambda p: True).create_authorized_issue(p)
        self.assertFalse(self.calls)

    def test_invalid_digest_rejected(self):
        with self.assertRaises(bridge.AdmissionDenied):
            self.client(admit=lambda p: True).create_authorized_issue(
                self.packet(goal_digest="not-a-sha")
            )
        self.assertFalse(self.calls)

    def test_authorized_create_and_readback(self):
        result = self.client(admit=lambda p: True).create_authorized_issue(
            self.packet()
        )
        self.assertEqual(len(self.calls), 2)
        self.assertEqual(self.calls[0].get_method(), "POST")
        self.assertEqual(self.calls[1].get_method(), "GET")
        self.assertEqual(result["issue_id"], "task-123")
        self.assertFalse(result["outcome_verified"])
        self.assertFalse(result["execution_verified"])
        self.assertEqual(len(result["idempotency_key"]), 64)

    def test_idempotency_key_stable_on_retry(self):
        client = self.client(admit=lambda p: True)
        key1 = client.create_authorized_issue(self.packet())["idempotency_key"]
        key2 = client.create_authorized_issue(
            self.packet(title="Same authorized WorkPacket")
        )["idempotency_key"]
        self.assertEqual(key1, key2)

    def test_wrong_company_readback_rejected(self):
        def wrong(request, timeout):
            if request.get_method() == "POST":
                return Response({"id": "task-123"})
            return Response({"id": "task-123", "companyId": "another-company",
                             "projectId": "project-123"})
        client = bridge.PaperclipAPI("https://paperclip.example.test", "x"*40,
                                     admit=lambda p: True, transport=wrong)
        with self.assertRaisesRegex(bridge.PaperclipError, "Company mismatch"):
            client.create_authorized_issue(self.packet())

    def test_wrong_project_readback_rejected(self):
        def wrong(request, timeout):
            if request.get_method() == "POST":
                return Response({"id": "task-123"})
            return Response({"id": "task-123", "companyId": "company-123",
                             "projectId": "another-project"})
        client = bridge.PaperclipAPI("https://paperclip.example.test", "x"*40,
                                     admit=lambda p: True, transport=wrong)
        with self.assertRaisesRegex(bridge.PaperclipError, "Project mismatch"):
            client.create_authorized_issue(self.packet())

    def test_only_https_origin_allowed(self):
        for url in ("http://localhost:3100", "https://a.example/path",
                    "https://user:pass@a.example", "https://a.example/?q=1"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                bridge.PaperclipAPI(url, "x" * 40)


if __name__ == "__main__":
    unittest.main()
