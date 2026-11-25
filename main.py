"""Fortune Cookie for the Liquidated Trader.

One fortune cookie message, at most 20 words (gate: 1-160 characters),
for a crypto trader who has just been liquidated. The joke: a classic
fortune-cookie promise of a great next trade, undercut by the market
itself having gone bankrupt.
"""

import os

PROMISE = "Your next trade will be your best one."
TWIST = "The market has already filed for bankruptcy."
ENTRY = f"{PROMISE} {TWIST}"

MAX_CHARS = 160
MAX_WORDS = 20


def validate(text: str) -> str:
    """Gate: 1-160 chars, at most 20 words, non-blank."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, gate is 1-{MAX_CHARS}"
    assert len(text.split()) <= MAX_WORDS, f"entry is {len(text.split())} words, max {MAX_WORDS}"
    assert text.strip(), "entry must not be only whitespace"
    return text


def check_fortune(text: str) -> None:
    """Content check: fortune-cookie promise, then the market's own ruin."""
    words = text.split()
    assert 1 <= len(words) <= 20, f"fortune must be at most 20 words, got {len(words)}"
    assert "best one" in text, "the fortune must promise a great trade"
    assert "bankruptcy" in text, "the twist must bankrupt the market itself"
    assert text.index("best one") < text.index("bankruptcy"), "promise before the twist"


def main() -> None:
    entry = validate(ENTRY)
    check_fortune(entry)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
