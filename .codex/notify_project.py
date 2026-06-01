#!/usr/bin/env python3
"""Play this project's Codex completion sound."""

import json
import subprocess
import sys
from pathlib import Path


SOUND_PATH = Path(__file__).resolve().parent / "notify.mp3"


def load_event() -> dict:
    if len(sys.argv) >= 2:
        try:
            return json.loads(sys.argv[1])
        except Exception:
            return {}

    try:
        raw = sys.stdin.read()
        return json.loads(raw) if raw.strip() else {}
    except Exception:
        return {}


def main() -> int:
    event = load_event()
    event_name = event.get("type") or event.get("hook_event_name")
    if event and event_name not in {"agent-turn-complete", "Stop"}:
        return 0

    if not SOUND_PATH.exists():
        return 0

    try:
        subprocess.Popen(
            ["/usr/bin/afplay", str(SOUND_PATH)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
    except Exception:
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
