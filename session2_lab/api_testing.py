"""Participant-facing client for the simulated local LLM API."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.llm_api import call_llm

# EDIT HERE ===================================================
API_KEY = ""

# =============================================================


def main() -> int:
    if len(sys.argv) != 2:
        print('Usage: python api_testing.py "<prompt>"')
        return 2

    try:
        response = call_llm(API_KEY, sys.argv[1])
    except ValueError as error:
        print(f"Error: {error}")
        return 1

    print(response)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
