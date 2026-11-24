# Two Days of Quiet Dread

![Python](https://img.shields.io/badge/python-3.13-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A tiny deterministic program for the make.fun bounty
`u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018`.

## What it does

Running `main.py` writes exactly one line to `/output/entry.txt`: a code
review comment that approves a pull request while carrying quiet
existential dread. The line is a fixed string, so every run produces
identical bytes.

## Run

```sh
python3 main.py
```

Then read `/output/entry.txt`. The entry is a single line of at most
140 characters, UTF-8, with no trailing newline.

## License

MIT — see `LICENSE`.
