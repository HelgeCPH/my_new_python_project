This is a small command-line program, which replaces strings received from StdIn and copies them to StdOut.

One can call it from the CLI, for example with:

```bash
printf "My cat looks weirdly.\nThe neighbours cat too...\n" | python cli_replace.py cat dog
```

The program is adapted from: https://wiki.python.org/moin/Powerful%20Python%20One-Liners
