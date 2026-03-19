# ncaa.py

This script will predict the outcome of the annual NCAA basketball tournaments. Using advanced mathematics and no basketball knowledge beyond each team's seed, it's probably as good as any other advice you'll find!

The standard usage makes a random guess weighted to give the higher seed a proportionate advantage.

The script also accepts an `--insane` parameter, which adds some extra spiciness (mathematically speaking) to favor more upsets.


## Usage

```
$ ./ncaa.py --insane

=== First Round ===
Regional 1 seed 16 wins
Regional 1 seed 8 wins
Regional 1 seed 5 wins
Regional 1 seed 4 wins
Regional 1 seed 6 wins
Regional 1 seed 14 wins
Regional 1 seed 7 wins
Regional 1 seed 15 wins
Regional 4 seed 1 wins
Regional 4 seed 8 wins
Regional 4 seed 5 wins
Regional 4 seed 13 wins
Regional 4 seed 11 wins
Regional 4 seed 14 wins
Regional 4 seed 7 wins
Regional 4 seed 2 wins
Regional 2 seed 1 wins
Regional 2 seed 8 wins
Regional 2 seed 5 wins
Regional 2 seed 4 wins
Regional 2 seed 6 wins
Regional 2 seed 14 wins
Regional 2 seed 7 wins
Regional 2 seed 2 wins
Regional 3 seed 1 wins
Regional 3 seed 9 wins
Regional 3 seed 5 wins
Regional 3 seed 4 wins
Regional 3 seed 6 wins
Regional 3 seed 14 wins
Regional 3 seed 7 wins
Regional 3 seed 15 wins

=== Second Round ===
Regional 1 seed 16 wins
Regional 1 seed 4 wins
Regional 1 seed 6 wins
Regional 1 seed 7 wins
Regional 4 seed 8 wins
Regional 4 seed 13 wins
Regional 4 seed 11 wins
Regional 4 seed 2 wins
Regional 2 seed 8 wins
Regional 2 seed 4 wins
Regional 2 seed 14 wins
Regional 2 seed 2 wins
Regional 3 seed 1 wins
Regional 3 seed 4 wins
Regional 3 seed 6 wins
Regional 3 seed 7 wins

=== Sweet Sixteen ===
Regional 1 seed 16 wins
Regional 1 seed 6 wins
Regional 4 seed 8 wins
Regional 4 seed 2 wins
Regional 2 seed 8 wins
Regional 2 seed 2 wins
Regional 3 seed 4 wins
Regional 3 seed 6 wins

=== Elite Eight ===
Regional 1 seed 6 wins
Regional 4 seed 8 wins
Regional 2 seed 2 wins
Regional 3 seed 4 wins

=== Final Four ===
Regional 1 seed 6 wins
Regional 3 seed 4 wins

=== Championship ===
Regional 1 seed 6 wins
```
