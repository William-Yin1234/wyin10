# Ethan Shenker, Alvin Wu, William Yin
# SoftDev
# K05 -- Random Team Member Selector
# 2020-09-05

# We interpreted the assignment as taking an input from the user representing what team they'd like to select a member from,
# and then outputting a random member from that team.

from random import randint as r

KREWES = {
    'orpheus': ['ERIC', 'SAUVE', 'JONATHAN', 'PAK', 'LIAM', 'WINNIE', 'KELLY', 'JEFFREY', 'KARL', 'ISHITA', 'VICTORIA', 'BENJAMIN', 'ARIB', 'AMELIA', 'CONSTANCE', 'IAN'],
    'rex': ['ANYA', 'DUB-Y', 'JESSICA', 'ALVIN', 'HELENA', 'MICHELLE', 'SHENKER', 'ARI', 'STELLA', 'RENEE', 'MADELYN', 'MAC', 'RYAN', 'DRAGOS'],
    'endymion': ['JASON', 'DEAN', 'MADDIE', 'SAQIF', 'CINDY', 'YI LING', 'RUOSHUI', 'FB', 'MATTHEW', 'MAY', 'ERIN', 'MEIRU']
}


def get_team_name(dic: dict) -> str:
    team_name = input(
        "Please enter the name of the team you'd like to select a member from: ").lower()
    while team_name not in dic:  # ensures team name provided exists
        # ensures we don't encounter a keyError
        team_name = input("Please enter a valid team name: ").lower()
    return team_name


def get_team_member(dic: dict, team_name: str) -> str:
    team_members = dic[team_name]
    index = r(0, len(team_members) - 1)  # selects random member
    return team_members[index]


def main():
    team_name = get_team_name(KREWES)
    team_member = get_team_member(KREWES, team_name)
    print(f"Team member {team_member} chosen from team {team_name}.")


main()