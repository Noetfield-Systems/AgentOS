#!/usr/bin/env python3
"""Test first-class AgentOS alternative-first entrypoint and recovery law."""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
RULE=".cursor/rules/010-execution-first-alternatives.mdc"

def main():
    root=(ROOT/"AGENTS.md").read_text(encoding="utf-8")
    rule=(ROOT/RULE).read_text(encoding="utf-8")
    for name,ok in (
        ("AGENTS entrypoint",RULE in root),
        ("automatic agent rule","alwaysApply: true" in rule),
        ("execution loop","DISCOVER -> SELECT -> EXECUTE -> VERIFY -> LEARN" in rule),
        ("do not stop on free provider","failing free API block an authorized, available paid API" in rule),
        ("original WorkPacket","original WorkPacket" in rule),
        ("independent verification","independent verifier" in rule),
        ("no fake revenue","a plan as execution" in rule),
        ("no needless founder report","Report only what changed" in rule),
    ):
        if not ok: raise SystemExit("FAIL AgentOS alternative-first law: "+name)
    print("PASS AgentOS P0 alternative-first always-on law")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
