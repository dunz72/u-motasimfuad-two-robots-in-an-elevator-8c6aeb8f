"""Two Robots in an Elevator — entry copier.

Reads entry.txt next to this script and copies its exact bytes to
$MAKEFUN_OUTPUT_DIR/entry.txt (or ./output/entry.txt when the env var
is unset). Stdlib only.
"""

import os
import sys
from pathlib import Path

MAX_CHARS = 200


def read_entry(source: Path) -> bytes:
    """Return the raw bytes of entry.txt, or exit with an error."""
    if not source.is_file():
        fail("entry.txt not found next to main.py")
    data = source.read_bytes()
    if not data:
        fail("entry.txt is empty")
    return data


def decode_entry(data: bytes) -> str:
    """Decode entry bytes as UTF-8 text."""
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        fail("entry.txt is not valid UTF-8")


def validate_line(text: str) -> str:
    """Check the entry is one non-empty line within the char limit."""
    line = text.rstrip("\n")
    if not line.strip():
        fail("entry.txt contains no text")
    if "\n" in line or "\r" in line:
        fail("entry must be a single line")
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in line):
        fail("entry contains a control character")
    if len(line) > MAX_CHARS:
        fail(
            f"entry line is {len(line)} characters, over the "
            f"{MAX_CHARS}-character limit"
        )
    return line


def resolve_output_dir(here: Path) -> Path:
    """Pick the output directory from the env var, else ./output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or str(here / "output")
    return Path(out_dir)


def write_output(out_path: Path, data: bytes) -> None:
    """Write the exact entry bytes to the output path."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(data)


def fail(message: str) -> None:
    """Print an error and exit non-zero."""
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def main() -> int:
    here = Path(__file__).resolve().parent
    data = read_entry(here / "entry.txt")
    text = decode_entry(data)
    line = validate_line(text)

    out_path = resolve_output_dir(here) / "entry.txt"
    write_output(out_path, data)

    print(f"wrote {len(data)} bytes ({len(line)} chars) to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
