#!/usr/bin/env python3
"""Basic hash type identifier"""

import sys
import re

HASH_PATTERNS = {
    "MD5": r"^[a-fA-F0-9]{32}$",
    "SHA-1": r"^[a-fA-F0-9]{40}$",
    "SHA-256": r"^[a-fA-F0-9]{64}$",
    "SHA-512": r"^[a-fA-F0-9]{128}$",
    "NTLM": r"^[a-fA-F0-9]{32}$",  # same length as MD5, context needed
}

def identify(hash_str):
    hash_str = hash_str.strip()
    matches = []
    for name, pattern in HASH_PATTERNS.items():
        if re.match(pattern, hash_str):
            matches.append(name)
    return matches

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <hash>")
        sys.exit(1)

    results = identify(sys.argv[1])
    if results:
        print("Possible hash types:")
        for r in results:
            print(f"  - {r}")
    else:
        print("Unknown or unsupported hash type")

if __name__ == "__main__":
    main()
