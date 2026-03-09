# Sarah Walker
# display final record for a home team

def final_record(home_team, teams) :
    results = teams[home_team]
    wins = results.count("W")
    losses = results.count("L")
    total = len(results)

    print(f"\nFinal Results for {home_team}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Winning Percentage: {wins / total * 100:.2f}%")

# teams = {
#         "BYU": ["W", "L", "W"],
#         "UVU": ["L", "W", "L"]
# }

# final_record("BYU", teams)