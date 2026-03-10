# Sarah Walker
# display final record for a home team

def final_record(home_team, team_records) :
    # prevent from running if home_team is not in list
    if home_team not in team_records :
        print(f"No record found for {home_team}")
        return

    # [0] is wins and [1] is losses
    wins = team_records[home_team][0]
    losses = team_records[home_team][1]
    total = wins + losses
    winning_percentage = wins / total * 100

    print(f"\nFinal Results for {home_team}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Winning Percentage: {winning_percentage:.2f}%")

    # determine printed result statement based on winning percentage
    if (winning_percentage >= 75) :
        print("NCAA Tournament bound!")
    elif (winning_percentage >= 50) :
        print("Good season!")
    else :
        print("Back to practice!")
