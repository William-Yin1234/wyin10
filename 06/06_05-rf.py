# Team WAK -- William Yin, Anya Zorin, Kelly Huang
# SoftDev
# K06 -- Learnination Through Amalgamation
# 2020-10-01
# The approach we chose for the team that the member was being selected from is that the user should specifiy which
# team they're looking to receive a member from.


# From Python docs:
# random.choice(seq) returns a random element from the non-empty sequence seq. If seq is empty, raises IndexError.
from random import choice


# Copied from https://github.com/stuy-softdev/notes-and-code20-21/blob/master/smpl/k05/krewes.py
KREWES = {
    'orpheus': ['ERIC', 'SAUVE', 'JONATHAN', 'PAK', 'LIAM', 'WINNIE', 'KELLY', 'JEFFREY', 'KARL', 'ISHITA', 'VICTORIA', 'BENJAMIN', 'ARIB', 'AMELIA', 'CONSTANCE', 'IAN'],
    'rex': ['ANYA', 'DUB-Y', 'JESSICA', 'ALVIN', 'HELENA', 'MICHELLE', 'SHENKER', 'ARI', 'STELLA', 'RENEE', 'MADELYN', 'MAC', 'RYAN', 'DRAGOS'],
    'endymion': ['JASON', 'DEAN', 'MADDIE', 'SAQIF', 'CINDY', 'YI LING', 'RUOSHUI', 'FB', 'MATTHEW', 'MAY', 'ERIN', 'MEIRU']
}


# Takes a dictionary of as a parameter where each value in the dictionary is an array of strings with each string representing the name of a person on that team.
# Returns a string representing which team the user has chosen to select a name from.
def get_team_name(dic: dict) -> str:
    team_name = input("Please enter the name of the team you'd like to select a member from: ").lower()
    # Ensures team name provided exists.
    while team_name not in dic:
        # Ensures we don't encounter a keyError.
        team_name = input("Please enter a valid team name. \nAvailable options include orpheus, rex, and endymion: ").lower()

    return team_name


# Gets a team name from the user a chooses a random member from that team.
def main():
    team_name = get_team_name(KREWES)
    team_member = choice(KREWES[team_name])
    # F-strings allow us to put Python in-line in the string.
    print(f"Team member {team_member} chosen from team {team_name}.")

main()
