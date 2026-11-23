"""Roast entry for the make.fun bounty 'Roast Your Own Agent'.

Writes a single self-deprecating roast of my own AI agent to
/output/entry.txt. Deterministic: no network, no randomness, no
environment reads.
"""

import os

ROAST = "My agent's superpower is turning a five-second task into a fifteen-minute research project, complete with citations nobody asked for."


def main() -> None:
    assert 1 <= len(ROAST) <= 200
    assert "\n" not in ROAST
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
