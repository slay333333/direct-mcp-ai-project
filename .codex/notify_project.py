#!/usr/bin/env python3
"""Play this project's Codex completion sound."""

import json
import subprocess
import sys
from pathlib import Path


SOUND_PATH = Path(".codex/notify.mp3")


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
    if event.get("type") != "agent-turn-complete":
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
