# Sarah Walker
# display final record for a home team

def final_record(home_team, teams) :
    results = teams[home_team]
    wins = results.count("W")
    losses = results.count("L")
    total = len(results)
    winning_percentage = wins / total * 100

    print(f"\nFinal Results for {home_team}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Winning Percentage: {winning_percentage:.2f}%")
    if (winning_percentage >= 75) :
        print("NCAA Tournament bound!")
    elif (winning_percentage >= 50) :
        print("Good season!")
    else :
        print("Back to practice!")

# teams = {
#         "BYU": ["W", "L", "W"],
#         "UVU": ["L", "W", "L"]
# }

# final_record("BYU", teams)