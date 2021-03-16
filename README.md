# ncaa.py

This script will predict the outcome of a single 16-team region of the NCAA men's basketball tournament. Using advanced mathematics and no basketball knowledge beyond each team's seed, it's probably as good as any other advice you'll find!

The standard usage makes a random guess weighted to give the higher seed a proportionate advantage. If a 1 seed is playing a 3 seed, the higher seed should win about 3/4 of the time.

The script also accepts an `--insane` parameter, which adds some extra spiciness (mathematically speaking) to enable more upsets.


## Usage

```
$ ./ncaa.py --insane

Round 1
1 wins (first)
8 wins (first)
5 wins (first)
13 wins (second)
11 wins (second)
14 wins (second)
10 wins (second)
2 wins (first)

Round 2
1 wins (first)
5 wins (first)
14 wins (second)
2 wins (second)

Round 3
5 wins (second)
2 wins (second)

Round 4
2 wins (second)
```
