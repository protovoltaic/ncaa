#!/usr/bin/env python3

from random import randint
from math import sqrt
import argparse


def pick(seed1, seed2):
    rand_pick = randint(1, seed1 + seed2)
    if rand_pick > seed1:
        return [seed1, 'first']
    else:
        return [seed2, 'second']


def insanepick(seed1, seed2):
    # First, geometrically reduce the difference to make an upset easier
    if seed1 > seed2:
        crazy_seed1 = int(round(seed2 + sqrt(seed1 - seed2)))
        crazy_seed2 = seed2
    else:
        crazy_seed1 = seed1
        crazy_seed2 = int(round(seed1 + sqrt(seed2 - seed1)))

    # Now also add a random value to each one. On average, this distribution
    # will equalize the seeds. On any one run, it won't.
    crazy_seed1 = crazy_seed1 + randint(1, crazy_seed2)
    crazy_seed2 = crazy_seed2 + randint(1, crazy_seed1)

    rand_pick = randint(1, crazy_seed1 + crazy_seed2)

    if rand_pick > crazy_seed1:
        return [seed1, 'first']
    else:
        return [seed2, 'second']


parser = argparse.ArgumentParser()
parser.add_argument('--insane', action='store_true', help='Go insane?')
args = parser.parse_args()

# Iterate over a 16-team quarter
seeds = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
tournament_round = 1

while(len(seeds) > 1):
    print('\nRound {}'.format(tournament_round))
    next_round_seeds = []

    while(len(seeds) > 0):
        seed1 = seeds.pop(0)
        seed2 = seeds.pop(0)
        if args.insane:
            [winner, order] = insanepick(seed1, seed2)
        else:
            [winner, order] = pick(seed1, seed2)
        print('{} wins ({})'.format(winner, order))
        next_round_seeds.append(winner)

    seeds = next_round_seeds
    tournament_round += 1

