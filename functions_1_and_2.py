# Jason 
# the first two functions for the functions are us project
# the first function introduction() displays the started menu and gets the name to start
# the second function displays the menu for the following calculations and returns and choice

def introduction():
    """
    Displays the introduction and game rules, prompts for the user's name.
    Returns the player's name to be used throughout the program.
    """
    print("=" * 50)
    print("   Welcome to the Women's Soccer Season Simulator!")
    print("=" * 50)
    print("\nHow it works:")
    print("  - Choose your home team from a list of teams")
    print("  - Pick how many games to play in the season")
    print("  - Face off against opponent teams each game")
    print("  - Scores are randomly generated (0-3, no ties)")
    print("  - Win 75% of games: NCAA Tournament bound!")
    print("  - Win 50-74%: Good season!")
    print("  - Under 50%: Back to practice!\n")

    player_name = input("Enter your name to get started: ")
    print(f"\nWelcome, {player_name}! Let's play some soccer!\n")
    return player_name

def display_menu():
    """
    Displays the main menu options and returns the user's validated choice.
    Returns the choice as a string ('1', '2', or '3').
    """
    print("\n--- MAIN MENU ---")
    print("1. Start a New Season")
    print("2. View How to Play")
    print("3. Quit")

    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Out of range. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number, not letters or symbols.")





