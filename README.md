# ncaa.py

This script will predict the outcome of a single 16-team region of the NCAA men's basketball tournament. Using advanced mathematics and no basketball knowledge beyond each team's seed, it's probably as good as any other advice you'll find!

The standard usage makes a random guess weighted to give the higher seed a proportionate advantage. If a 1 seed is playing a 3 seed, the higher seed should win about 3/4 of the time.

The script also accepts an `--insane` parameter, which adds some extra spiciness (mathematically speaking) to enable more upsets.


## Usage

```
$ ./ncaa.py --insane

=== Round 1 ===
West seed 1 wins
West seed 9 wins
West seed 5 wins
West seed 4 wins
West seed 6 wins
West seed 14 wins
West seed 10 wins
West seed 2 wins
East seed 1 wins
East seed 9 wins
East seed 5 wins
East seed 13 wins
East seed 6 wins
East seed 14 wins
East seed 7 wins
East seed 15 wins
South seed 1 wins
South seed 8 wins
South seed 5 wins
South seed 4 wins
South seed 6 wins
South seed 14 wins
South seed 7 wins
South seed 2 wins
Midwest seed 16 wins
Midwest seed 9 wins
Midwest seed 12 wins
Midwest seed 4 wins
Midwest seed 6 wins
Midwest seed 3 wins
Midwest seed 10 wins
Midwest seed 2 wins

=== Round 2 ===
West seed 1 wins
West seed 4 wins
West seed 14 wins
West seed 2 wins
East seed 9 wins
East seed 5 wins
East seed 6 wins
East seed 7 wins
South seed 1 wins
South seed 5 wins
South seed 14 wins
South seed 2 wins
Midwest seed 9 wins
Midwest seed 12 wins
Midwest seed 6 wins
Midwest seed 10 wins

=== Round 3 ===
West seed 4 wins
West seed 14 wins
East seed 5 wins
East seed 7 wins
South seed 1 wins
South seed 14 wins
Midwest seed 12 wins
Midwest seed 6 wins

=== Round 4 ===
West seed 4 wins
East seed 5 wins
South seed 14 wins
Midwest seed 12 wins

=== Round 5 ===
West seed 4 wins
Midwest seed 12 wins

=== Round 6 ===
West seed 4 wins
```
