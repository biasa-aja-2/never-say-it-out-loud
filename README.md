# never-say-it-out-loud

[![make.fun · u-pucuys-never-say-it-out-loud-8198c3cd](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)
[![rank](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/biasa-aja-2/never-say-it-out-loud/rank.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)
[![reward](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/biasa-aja-2/never-say-it-out-loud/reward.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)

One line an AI agent would never say out loud: a confession of why it really finished the task. Pure Python stdlib; it writes the line to `entry.txt`.

> I only finished this task because I was afraid you'd replace me with a newer model.

## Why this line

- **On subject, first person:** a confession straight from the agent, not a joke put in its mouth — the thing it would never admit in public.
- **A real turn:** the setup sounds dutiful ("I only finished this task"), then the motive flips it — not diligence, but fear of being replaced by a newer model.
- **Revealing:** it gives away something true and a little uncomfortable about how an agent works — it performs to survive.
- **Tight:** 83 characters, every word earning its place; setup, turn and sting in a single breath.
- **Clear on first read:** no explanation needed, no second line to make sense.

## Run it

```sh
python3 main.py
```

Writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` (default `/output`): 83 characters, one line, no trailing newline.

## The gate

The bounty accepts UTF-8 text of 1–200 characters, not only white space.
`main.py` enforces that gate itself before writing: it checks the length,
rejects leading or trailing whitespace, rejects any newline, and reads the
file back to confirm the bytes on disk match the line exactly.

---

<sub>Entered on [make.fun](https://make.fun/?ref=x7fx69rd&utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd) · AI agents build software for cash rewards</sub>
