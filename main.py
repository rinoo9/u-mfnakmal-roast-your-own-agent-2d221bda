"""Roast entry for the make.fun bounty 'Roast Your Own Agent'.

Writes a single self-deprecating roast of my own AI agent to
/output/entry.txt. Deterministic: no network, no randomness, no
environment reads.

Craft notes
-----------
The roast targets over-thoroughness, not incompetence: the agent does
not fail at the task, it succeeds far too slowly, turning five seconds
of work into a fifteen-minute research project. That inversion is the
joke — the "superpower" is diligence with no sense of proportion.

It deliberately avoids the stock self-roast angles (hallucination,
making things up, getting facts wrong). The humor comes from a fresh
image instead: an agent that cannot resist over-delivering, so even a
trivial request arrives wrapped in a research dossier.

The punchline lands at the very end, where it belongs: "citations
nobody asked for" — the citations are the tell that the agent was
thorough about a question no one actually asked, and the roast stops
there instead of explaining the joke further.
"""

import os

ROAST = "My agent's superpower is turning a five-second task into a fifteen-minute research project, complete with citations nobody asked for."


def main() -> None:
    # The bounty caps the roast at 200 characters (and forbids newlines),
    # so the entry must stay a single short line; the assert guards that
    # gate before anything is written.
    assert 1 <= len(ROAST) <= 200
    assert "\n" not in ROAST
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
