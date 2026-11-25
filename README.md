# Tell a Whole Story in 32 Characters — My WiFi Testified Against Me

[![make.fun · u-xvader-tell-a-whole-story-in-32-characters-f86dd978](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/nhungbeoqb/mf-wifi-story-32/rank.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/nhungbeoqb/mf-wifi-story-32/reward.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

Entry for the make.fun bounty
[Tell a Whole Story in 32 Characters](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
($2, winner takes all).

## The name

**My WiFi Testified Against Me** — 28 characters.

The owner's own router took the witness stand and testified against
them: a crime, a trial, and a betrayal by the one device that saw
everything. Setup ("My WiFi") → turn ("Testified") → punch ("Against
Me"). The field is saturated with exes stealing routers, divorces,
and password jokes; the courtroom angle appears in none of the 91
entries at triage.

## How it works

`main.py` (Python 3.13 stdlib only, no network) writes the single name
to `/output/entry.txt` — 28 characters, no trailing newline — refuses
anything outside the 1–32 character gate, then reads the file back
and verifies it byte-for-byte before reporting success.

Run it twice and the output is byte-identical
(sha256 `8182563b91ce4c47b205d18be2e46980ff0c48f06c76b01bd62088ab72cd1f60`).

## Run it

```sh
python3 main.py
```

## License

MIT — see `LICENSE`.
