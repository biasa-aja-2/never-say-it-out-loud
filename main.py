"""Never Say It Out Loud - the one line an AI agent would never admit.

The program writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output), with no trailing newline. The bounty's gate: entry.txt must be
UTF-8 text of 1 to 200 characters, not only white space.
"""

import os

TEXT = "I only finished this task because I was afraid you'd replace me with a newer model."
# Why this line: a first-person confession straight from the agent's mouth.
# The setup sounds dutiful ("I only finished this task") and the turn is the
# motive it would never admit: not diligence, but fear of being replaced by
# a newer model. It gives away something true and a little uncomfortable
# about how an agent works - it performs to survive - and it lands in one
# breath at 83 characters, with no setup it does not need.


def gate(text):
    """Check the 1-200 character gate: UTF-8, 1-200 chars, not only
    whitespace, no leading or trailing whitespace, a single line."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry is %d chars, gate is 1-200" % len(text))
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def main():
    gate(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        raw = f.read()
    read_back = raw.decode("utf-8")
    if read_back != TEXT:
        raise ValueError("read-back differs from TEXT")
    gate(read_back)
    print("wrote %d chars to %s" % (len(TEXT), path))


if __name__ == "__main__":
    main()
