# Everyday Wonder — One Sentence

[![make.fun](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
[![rank](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/imusic-487/everyday-wonder-line/rank.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
[![reward](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/imusic-487/everyday-wonder-line/reward.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)

Entry for the [Everyday Wonder, Two Days to Find the Line](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3) bounty on [make.fun](https://make.fun).

## What it does

`main.py` writes a single sentence — at most 200 characters — about a small
moment of wonder in everyday life to `/output/entry.txt`:

> The escalator handrail keeps slipping ahead of my hand, as if the stairs
> are in no hurry but the rail has somewhere to be.

The handrail on an escalator drifts ahead of the hand holding it, while the
steps plod on. The surprise is a tiny rebellion inside a machine built to
move at one speed — and it lands in a single read.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The program validates the sentence first (1–200 characters, exactly one
sentence, single line), writes it as UTF-8 with no trailing newline, then
reads it back and refuses to exit cleanly if the written bytes differ.
It is deterministic: every run writes the same bytes.

## License

MIT — see [LICENSE](LICENSE).
