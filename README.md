# Two Robots in an Elevator

One awkward line of robot small talk, spoken by one robot to another
while sharing an elevator ride. A proximity sensor reading, a firmware
update, and a robot that is still buffering.

[![make.fun · u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/dunz72/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/rank.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/dunz72/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/reward.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

Built for the [make.fun bounty](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f) — see the bounty page on [make.fun](https://make.fun) for the rules and leaderboard.

## Entry

> My proximity sensor reports we are 0.4 meters apart — the closest I have stood to anyone since my last firmware update, and I am still buffering.

## How it works

`main.py` (stdlib only) reads `entry.txt` next to it and copies its exact
bytes to `$MAKEFUN_OUTPUT_DIR/entry.txt`, validating that the line exists,
is non-empty, and is at most 200 characters.

---
