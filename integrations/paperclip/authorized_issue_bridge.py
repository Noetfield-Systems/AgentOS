#!/usr/bin/env python3
"""Permit-gated Paperclip Issue adapter, reusable by the owned Noetfield fork.

This adapter does NOT issue Governor permits or verify business outcomes.
The caller must inject a real, trusted admission function backed by the
existing Governor/NAC. No admission callback means no issue can be created.
"""
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Callable, Any
from urllib.error import HTTPError
from urllib.parse import urlparse
from urllib.request import Request, build_opener, HTTPRedirectHandler

_ID = re.compile(r"^[A-Za-z0-9_-]{1,128}$")
_SHA256 = re.compile(r"^[a-f0-9]{64}$")
_MAX_RESPONSE = 262144


class AdmissionDenied(Exception):
    pass


class PaperclipError(Exception):
    pass


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise PaperclipError("Redirect refused: credentials cannot be forwarded")


@dataclass(frozen=True)
class WorkPacket:
    company_id: str                 # Paperclip UUID, not the portfolio slug
    project_id: str                 # Paperclip project UUID
    workpacket_id: str              # Existing NAC-issued stable ID
    title: str
    description: str
    goal_digest: str                # sha256 digest (hex) of Founder goal
    expires_at: str                 # UTC RFC3339 / ISO8601
    assignee_agent_id: str | None = None

    def validate(self) -> None:
        for name in ("company_id", "project_id", "workpacket_id"):
            if not _ID.fullmatch(getattr(self, name)):
                raise AdmissionDenied(f"Invalid {name}")
        if self.assignee_agent_id and not _ID.fullmatch(self.assignee_agent_id):
            raise AdmissionDenied("Invalid assignee_agent_id")
        if not self.title.strip() or len(self.title) > 240:
            raise AdmissionDenied("Invalid title")
        if not self.description.strip() or len(self.description) > 100000:
            raise AdmissionDenied("Invalid description")
        if not _SHA256.fullmatch(self.goal_digest):
            raise AdmissionDenied("Invalid goal digest")
        try:
            expiry = datetime.fromisoformat(self.expires_at.replace("Z", "+00:00"))
        except ValueError as exc:
            raise AdmissionDenied("Invalid expiry") from exc
        if expiry.tzinfo is None or expiry <= datetime.now(timezone.utc):
            raise AdmissionDenied("WorkPacket is expired or missing timezone")


class PaperclipAPI:
    def __init__(self, base_url: str, token: str,
                 admit: Callable[[WorkPacket], bool] | None = None,
                 transport: Callable[[Request, float], Any] | None = None):
        parsed = urlparse(base_url)
        if (parsed.scheme != "https" or not parsed.netloc or parsed.username
                or parsed.password or parsed.path not in ("", "/")
                or parsed.query or parsed.fragment):
            raise ValueError("Paperclip base_url must be an HTTPS origin only")
        if not token or len(token) < 20:
            raise ValueError("Paperclip service token is missing or malformed")
        self.base_url = base_url.rstrip("/")
        self.__token = token
        self.admit = admit
        self.transport = transport or (
            lambda request, timeout: build_opener(_NoRedirect()).open(
                request, timeout=timeout
            )
        )

    def _request(self, method: str, path: str, body: dict | None = None) -> dict:
        data = (json.dumps(body, separators=(",", ":"), sort_keys=True).encode()
                if body is not None else None)
        request = Request(
            self.base_url + "/api/" + path,
            method=method, data=data,
            headers={
                "Authorization": "Bearer " + self.__token,
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
        )
        try:
            with self.transport(request, 8.0) as response:
                raw = response.read(_MAX_RESPONSE + 1)
                if len(raw) > _MAX_RESPONSE:
                    raise PaperclipError("Response exceeds size limit")
                value = json.loads(raw)
                if not isinstance(value, dict):
                    raise PaperclipError("Unexpected response envelope")
                return value
        except HTTPError as exc:
            raise PaperclipError(f"Paperclip HTTP {exc.code} ({method})") from None

    def health(self) -> dict:
        return self._request("GET", "health")

    def get_issue(self, issue_id: str) -> dict:
        if not _ID.fullmatch(issue_id):
            raise ValueError("Invalid issue id")
        return self._request("GET", "issues/" + issue_id)

    def create_authorized_issue(self, packet: WorkPacket) -> dict:
        packet.validate()
        if self.admit is None or self.admit(packet) is not True:
            raise AdmissionDenied("Valid external Governor/NAC admission required")

        key_material = "\x1f".join((
            "noetfield-workpacket-v1", packet.company_id,
            packet.project_id, packet.workpacket_id
        ))
        idem = hashlib.sha256(key_material.encode()).hexdigest()
        description = (
            packet.description.rstrip() + "\n\n"
            "Noetfield authority reference (not a permit):\n"
            f"WorkPacket: {packet.workpacket_id}\n"
            f"Goal digest: sha256:{packet.goal_digest}\n"
            "Worker MUST independently recheck the signed Governor/NAC permit "
            "before any consequential effect."
        )
        body = {
            "title": packet.title,
            "description": description,
            "projectId": packet.project_id,
            "status": "todo",
            "idempotencyKey": idem,
        }
        if packet.assignee_agent_id is not None:
            body["assigneeAgentId"] = packet.assignee_agent_id

        issue = self._request(
            "POST", f"companies/{packet.company_id}/issues", body
        )
        issue_id = issue.get("id")
        if not isinstance(issue_id, str) or not _ID.fullmatch(issue_id):
            raise PaperclipError("Create returned no valid issue id")

        # Read back the exact issue rather than treating 2xx as proof of state.
        readback = self.get_issue(issue_id)
        if readback.get("id") != issue_id:
            raise PaperclipError("Issue id changed on readback")
        if readback.get("companyId") != packet.company_id:
            raise PaperclipError("Company mismatch on issue readback")
        if readback.get("projectId") != packet.project_id:
            raise PaperclipError("Project mismatch on issue readback")
        return {"issue_id": issue_id, "company_id": packet.company_id,
                "project_id": packet.project_id,
                "workpacket_id": packet.workpacket_id,
                "idempotency_key": idem,
                "status": "ISSUE_CREATED_AND_READ_BACK",
                "execution_verified": False,
                "outcome_verified": False}


__all__ = ["PaperclipAPI", "PaperclipError", "WorkPacket", "AdmissionDenied"]
