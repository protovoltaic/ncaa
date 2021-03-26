# ncaa.py

This script will predict the outcome of a single 16-team region of the NCAA men's basketball tournament. Using advanced mathematics and no basketball knowledge beyond each team's seed, it's probably as good as any other advice you'll find!

The standard usage makes a random guess weighted to give the higher seed a proportionate advantage. If a 1 seed is playing a 3 seed, the higher seed should win about 3/4 of the time.

The script also accepts an `--insane` parameter, which adds some extra spiciness (mathematically speaking) to enable more upsets.


## Usage

```
$ ./ncaa.py --insane

=== First Round ===
West seed 1 wins
West seed 9 wins
West seed 5 wins
West seed 13 wins
West seed 11 wins
West seed 3 wins
West seed 10 wins
West seed 15 wins
East seed 16 wins
East seed 9 wins
East seed 5 wins
East seed 4 wins
East seed 6 wins
East seed 14 wins
East seed 10 wins
East seed 2 wins
South seed 1 wins
South seed 9 wins
South seed 12 wins
South seed 4 wins
South seed 11 wins
South seed 3 wins
South seed 10 wins
South seed 2 wins
Midwest seed 16 wins
Midwest seed 8 wins
Midwest seed 12 wins
Midwest seed 13 wins
Midwest seed 11 wins
Midwest seed 3 wins
Midwest seed 7 wins
Midwest seed 15 wins

=== Second Round ===
West seed 1 wins
West seed 5 wins
West seed 11 wins
West seed 15 wins
East seed 16 wins
East seed 4 wins
East seed 14 wins
East seed 10 wins
South seed 9 wins
South seed 4 wins
South seed 3 wins
South seed 10 wins
Midwest seed 8 wins
Midwest seed 12 wins
Midwest seed 11 wins
Midwest seed 7 wins

=== Round of Sixteen ===
West seed 1 wins
West seed 15 wins
East seed 16 wins
East seed 10 wins
South seed 9 wins
South seed 10 wins
Midwest seed 8 wins
Midwest seed 7 wins

=== Elite Eight ===
West seed 1 wins
East seed 10 wins
South seed 10 wins
Midwest seed 8 wins

=== Final Four ===
West seed 1 wins
Midwest seed 8 wins

=== Championship ===
West seed 1 wins
```
