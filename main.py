# Sarah Walker, Jason Marks, Juliana Merkley, Porter Collins

# import all functions
from functions_1_and_2 import introduction, display_menu
from part3 import pick_teams
from play_game import play_game
from final_record import final_record

# welcome the user
introduction()

bContinue = True
# keep presenting the menu after function calls until user chooses to quit
while bContinue :
# call functions based on user selection
    user_choice = display_menu()
    if (user_choice == 1) :
        teams = pick_teams()
        game_results = play_game(teams)
        final_record(teams[0], game_results)
    elif (user_choice == 2) :
        introduction() 
    else :
        print("Thank you for playing!")
        # break the loop
        bContinue = False
