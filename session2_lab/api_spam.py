"""Simulate someone misusing a leaked API key by flooding the LLM API with calls."""

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.llm_api import SAFE_PROMPTS, call_llm

from api_testing import API_KEY

NUM_CALLS = 100


def main() -> int:
    for call_number in range(1, NUM_CALLS + 1):
        prompt = random.choice(SAFE_PROMPTS)
        try:
            call_llm(API_KEY, prompt)
        except ValueError as error:
            print(f"Error: {error}")
            return 1
        print(f"[{call_number}/{NUM_CALLS}] {prompt}")

    print(f"Sent {NUM_CALLS} calls using API key {API_KEY[:12]}...")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
