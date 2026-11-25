#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary - entry: Monday.

Writes exactly one word, "Monday", to /output/entry.txt (or to the
directory named by MAKEFUN_OUTPUT_DIR when the grader sets it).

Why Monday, against the judge's brief, in the order it weighs things:
  1. It names one real word to erase: Monday, a weekday every reader
     recognises at once - no explanation, no caption needed.
  2. The joke lands the moment the word is gone: erase Monday and the
     week jumps straight from Sunday to Tuesday. No more Monday blues,
     no more "case of the Mondays", no more alarm-clock dread - the
     weekend never has to end.
  3. The humour comes from the word itself and the gap it leaves: the
     most dreaded day on the calendar is the one the whole week is
     built around, so deleting it deletes the week's worst day and
     leaves a hole everyone can feel.
  4. It is fresh against the field: the obvious picks are already
     crowded - irregardless (40+ entries), queue (20+), moist (20+),
     literally, defenestration, colonel, lisp - while Monday is a
     plain, everyday word nobody had to invent, picked for the gap
     it leaves rather than for sounding strange.
  5. It is exact: one word, spelled correctly, nothing added around
     it - no trailing newline, no punctuation, no caption.
"""
import os

WORD = "Monday"
MAX_CHARS = 77


def main() -> None:
    assert WORD == WORD.strip(), "word must have no surrounding whitespace"
    assert " " not in WORD, "entry must be exactly one word"
    assert WORD.isalpha(), "entry must be letters only"
    assert WORD == WORD.capitalize(), "weekday must be capitalised"
    assert 1 <= len(WORD) <= MAX_CHARS, "entry must be 1-77 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Read back and verify: the file the judge reads must be exactly the
    # word, byte for byte - no newline, no caption, nothing added.
    with open(path, "rb") as f:
        written = f.read()
    assert written == WORD.encode("utf-8"), "entry.txt must hold only the word"
    print(WORD)


if __name__ == "__main__":
    main()
