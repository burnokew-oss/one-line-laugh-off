"""One-Line Laugh-Off — entry program (pure stdlib, deterministic).

Writes exactly one funny line to /output/entry.txt.
The line is judged against the published judge brief: a single joke that
lands on a cold read, with a hard sudden laugh, a surprise turn, every word
earning its place, and a fresh idea rather than a recycled setup.
"""

import hashlib
import os

OUTPUT_PATH = "/output/entry.txt"

# The setup is familiar (counting sheep) so the line lands cold with no
# explanation needed; the punchline turns it sideways — the sheep are not
# sleepy props, they are workers with a grievance. 80 characters, one line.
ENTRY_TEXT = "I tried counting sheep to fall asleep, but they unionised and demanded overtime."


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = ENTRY_TEXT.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(data)
    print("wrote %s (%d bytes, sha256 %s)" % (OUTPUT_PATH, len(data), hashlib.sha256(data).hexdigest()))


if __name__ == "__main__":
    main()
