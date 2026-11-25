#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters.

A Wi-Fi network name that lands a joke and implies a whole story in
the few words a passer-by sees in a phone's network list.

The line: "Ex took the dog. I kept WiFi."
A breakup in two sentences: the ex walked out with the dog, and the
narrator's consolation prize -- the thing they actually kept -- is the
Wi-Fi. Situation, character, and something that happened, in 29
characters. Pure standard library.
"""

import os

LINE = "Ex took the dog. I kept WiFi."


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 32 characters,
    # not only white space, a single line with no trailing newline.
    # A Wi-Fi name is also capped at 32 octets, so check the UTF-8
    # byte length too, and reject control characters: a network list
    # shows the name raw, and a stray control byte would corrupt it.
    assert LINE.strip(), "line must not be only white space"
    assert "\n" not in LINE, "line must be a single line"
    assert 1 <= len(LINE) <= 32, f"line is {len(LINE)} chars, gate is 1-32"
    assert len(LINE.encode("utf-8")) <= 32, "SSID is at most 32 octets"
    assert all(ord(c) >= 0x20 for c in LINE), "no control characters in an SSID"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
