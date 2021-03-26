# ncaa.py

This script will predict the outcome of the annual NCAA basketball tournaments. Using advanced mathematics and no basketball knowledge beyond each team's seed, it's probably as good as any other advice you'll find!

The standard usage makes a random guess weighted to give the higher seed a proportionate advantage.

The script also accepts an `--insane` parameter, which adds some extra spiciness (mathematically speaking) to favor more upsets.


## Usage

```
$ ./ncaa.py --insane

=== First Round ===
West seed 1 wins
West seed 8 wins
West seed 5 wins
West seed 4 wins
West seed 11 wins
West seed 3 wins
West seed 7 wins
West seed 2 wins
East seed 16 wins
East seed 8 wins
East seed 5 wins
East seed 4 wins
East seed 6 wins
East seed 14 wins
East seed 7 wins
East seed 2 wins
South seed 16 wins
South seed 8 wins
South seed 12 wins
South seed 13 wins
South seed 6 wins
South seed 14 wins
South seed 7 wins
South seed 2 wins
Midwest seed 1 wins
Midwest seed 9 wins
Midwest seed 5 wins
Midwest seed 4 wins
Midwest seed 6 wins
Midwest seed 14 wins
Midwest seed 7 wins
Midwest seed 2 wins

=== Second Round ===
West seed 1 wins
West seed 4 wins
West seed 11 wins
West seed 2 wins
East seed 16 wins
East seed 4 wins
East seed 6 wins
East seed 2 wins
South seed 16 wins
South seed 13 wins
South seed 6 wins
South seed 7 wins
Midwest seed 9 wins
Midwest seed 4 wins
Midwest seed 14 wins
Midwest seed 7 wins

=== Sweet Sixteen ===
West seed 4 wins
West seed 11 wins
East seed 4 wins
East seed 2 wins
South seed 13 wins
South seed 6 wins
Midwest seed 4 wins
Midwest seed 7 wins

=== Elite Eight ===
West seed 11 wins
East seed 2 wins
South seed 6 wins
Midwest seed 4 wins

=== Final Four ===
East seed 2 wins
South seed 6 wins

=== Championship ===
East seed 2 wins
```
