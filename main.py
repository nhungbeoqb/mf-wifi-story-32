#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters -- make.fun entry.

Writes a single Wi-Fi network name to /output/entry.txt.

The name: "My WiFi Testified Against Me" (28 characters).

The story it implies, in one line: the owner's own router took the
witness stand and testified against them -- a crime, a trial, and a
betrayal by the one device that saw everything. Setup ("My WiFi")
-> turn ("Testified") -> punch ("Against Me"). No ex, no router theft,
no divorce, no password joke: the field of 91 entries is saturated
with all of those, and the courtroom angle appears in none of them.
"""

import os
import sys

NAME = "My WiFi Testified Against Me"
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 32


def main() -> int:
    if not 1 <= len(NAME) <= MAX_CHARS:
        print(
            f"entry must be 1-{MAX_CHARS} characters, got {len(NAME)}",
            file=sys.stderr,
        )
        return 1
    if not NAME.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write exactly the name: no trailing newline, so the file holds
    # precisely the 28 characters the gate counts.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(NAME)
    # Read it back and verify: the sealed scorer reads this file, so a
    # partial write or an encoding surprise must fail loudly here
    # instead of shipping a file that does not match the name.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != NAME.encode("utf-8"):
        print("verification failed: file does not match the entry", file=sys.stderr)
        return 1
    if not 1 <= len(written.decode("utf-8")) <= MAX_CHARS:
        print("verification failed: file outside the 1-32 character gate", file=sys.stderr)
        return 1
    print(f"wrote {len(NAME)} characters to {OUTPUT_PATH} (verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
