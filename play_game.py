#Juliana Merkley

#runs the game simulation, using the teams decided in part 3
#also tracks wins and losses as a seasonal record to be used later
#randomizes scores and prevents ties

import random

# stores records for every team
teamRecords = {}

def play_game(lstTeams):

    # lstTeams variable comes from part3.py
    homeTeam = lstTeams[0]
    awayTeam = lstTeams[1]

    # create records if they don't exist yet
    if homeTeam not in teamRecords:
        teamRecords[homeTeam] = [0, 0]  # [wins, losses]

    if awayTeam not in teamRecords:
        teamRecords[awayTeam] = [0, 0]  # [wins, losses]

    # max random score is 3 like a5 soccer assignment
    homeScore = random.randint(0, 3)
    awayScore = random.randint(0, 3)

    # prevent ties
    while homeScore == awayScore:
        awayScore = random.randint(0, 3)

    print(f'\n{homeTeam}: {homeScore}')
    print(f'{awayTeam}: {awayScore}\n')

    #return win or loss and then update the team's seasonal record
    if homeScore > awayScore:
        print('W')
        teamRecords[homeTeam][0] += 1
        teamRecords[awayTeam][1] += 1
    else:
        print('L')
        teamRecords[homeTeam][1] += 1
        teamRecords[awayTeam][0] += 1