#!/usr/bin/env python3

from random import randint
from math import sqrt
import argparse


def pick(team1, team2, insane=False):
    if not insane:
        # Standard algorithm: each team gets a number of entries equal
        # to their seed, and if a team's entry is picked, they lose.
        # A 1 seed vs. a 5 seed would look like: [1,5,5,5,5,5]. Choosing
        # from that list at random would give a 1 in 6 upset chance.
        if randint(1, team1['seed'] + team2['seed']) > team1['seed']:
            return team1
        else:
            return team2
    else:
        # "Advanced" algorithm. Same idea as standard, but we mess with the
        # odds and embrace chaos. This mode tends to get the "best" results.
        #
        # First, geometrically reduce the difference between the seeds to
        # make an upset easier.
        if team1['seed'] > team2['seed']:
            insane_seed1 = int(round(
                team1['seed'] + sqrt(team1['seed'] - team2['seed'])
            ))
            insane_seed2 = team2['seed']
        elif team1['seed'] < team2['seed']:
            insane_seed1 = team1['seed']
            insane_seed2 = int(round(
                team2['seed'] + sqrt(team2['seed'] - team1['seed'])
            ))
        else: # Seeds are equal
            insane_seed1 = team1['seed']
            insane_seed2 = team2['seed']

        # Now also add a random value to each one. On average, this
        # distribution will equalize the seeds. On any one run,
        # it almost certainly won't.
        insane_seed1 = insane_seed1 + randint(1, insane_seed2)
        insane_seed2 = insane_seed2 + randint(1, insane_seed1)

        if randint(1, insane_seed1 + insane_seed2) > insane_seed1:
            return team1
        else:
            return team2


def simulate_tournament(teams, round_number, insane):
    if len(teams) == 1:
        return teams[0]
    else:
        winning_teams = []
        print('\n=== {} ==='.format(round_names[round_number]))
        while len(teams):
            winner = pick(
                teams.pop(0),
                teams.pop(0),
                insane
            )
            winning_teams.append(winner)
            print('{} seed {} wins'.format(
                winner['region'],
                winner['seed']
            ))
        # Recurse!
        return simulate_tournament(winning_teams, round_number + 1, insane)


parser = argparse.ArgumentParser()
parser.add_argument('--insane', action='store_true', help='Go insane?')
args = parser.parse_args()
if 'insane' not in args:
    args.insane = False

# Define some useful information about the tournament.
entry_order = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
round_names = {
    1: 'First Round', 2: 'Second Round', 3: 'Round of Sixteen',
    4: 'Elite Eight', 5: 'Final Four', 6: 'Championship'
}

# Build an ordered list of region:seed pairings to define initial matchups.
teams = []
for region in ('West', 'East', 'South', 'Midwest'):
    for seed in entry_order:
        teams.append({'seed': seed, 'region': region})

# Run the tournament.
simulate_tournament(teams, 1, args.insane)
