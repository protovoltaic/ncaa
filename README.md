# ncaa.py

This script will predict the outcome of the annual NCAA basketball tournaments. Using advanced mathematics and no basketball knowledge beyond each team's seed, it's probably as good as any other advice you'll find!

The standard usage makes a random guess weighted to give the higher seed a proportionate advantage.

The script also accepts an `--insane` parameter, which adds some extra spiciness (mathematically speaking) to favor more upsets.


## Usage

```
$ ./ncaa.py --insane

=== First Round ===
East seed 1 wins
East seed 8 wins
East seed 12 wins
East seed 4 wins
East seed 11 wins
East seed 14 wins
East seed 10 wins
East seed 15 wins
South seed 1 wins
South seed 8 wins
South seed 5 wins
South seed 4 wins
South seed 6 wins
South seed 3 wins
South seed 7 wins
South seed 2 wins
West seed 1 wins
West seed 8 wins
West seed 5 wins
West seed 13 wins
West seed 6 wins
West seed 14 wins
West seed 7 wins
West seed 2 wins
Midwest seed 1 wins
Midwest seed 9 wins
Midwest seed 5 wins
Midwest seed 4 wins
Midwest seed 11 wins
Midwest seed 3 wins
Midwest seed 10 wins
Midwest seed 2 wins

=== Second Round ===
East seed 8 wins
East seed 12 wins
East seed 14 wins
East seed 10 wins
South seed 1 wins
South seed 5 wins
South seed 3 wins
South seed 2 wins
West seed 8 wins
West seed 13 wins
West seed 14 wins
West seed 2 wins
Midwest seed 1 wins
Midwest seed 4 wins
Midwest seed 3 wins
Midwest seed 10 wins

=== Sweet Sixteen ===
East seed 8 wins
East seed 14 wins
South seed 5 wins
South seed 2 wins
West seed 8 wins
West seed 14 wins
Midwest seed 1 wins
Midwest seed 10 wins

=== Elite Eight ===
East seed 14 wins
South seed 2 wins
West seed 8 wins
Midwest seed 1 wins

=== Final Four ===
South seed 2 wins
West seed 8 wins

=== Championship ===
West seed 8 wins
```
