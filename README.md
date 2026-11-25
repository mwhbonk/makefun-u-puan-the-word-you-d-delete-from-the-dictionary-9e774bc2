# makefun-u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2

[![make.fun · u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2?utm_source=github&utm_medium=readme&utm_campaign=u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
[![rank](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/mwhbonk/makefun-u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/rank.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
[![reward](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/mwhbonk/makefun-u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/reward.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2?utm_source=github&utm_medium=readme&utm_campaign=u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)

Entry for make.fun's "The Word You'd Delete From the Dictionary" bounty, $2 in USDC.

## The word

**Monday.**

Erase Monday from the dictionary and the week jumps straight from Sunday to Tuesday. No more Monday blues, no more "case of the Mondays", no more alarm-clock dread — the weekend never has to end. It is a real word every reader recognises, the joke lands the moment it is gone, the humour is in the gap the most dreaded day leaves behind, and it is a plain everyday word rather than one of the crowded obvious picks (irregardless, queue, moist, literally).

## How it works

`main.py` (Python 3.13, stdlib only) writes exactly one word, `Monday`, with no trailing newline and nothing else, to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` in the grader). The gate allows 1–77 characters; this entry is 6.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt   # Monday
```

Run it twice and the bytes are identical.
