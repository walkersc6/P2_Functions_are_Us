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
# call functions in order
    user_choice = display_menu()
    if (user_choice == 1) :
        pick_teams()
        play_game()
        #final_record()
    elif (user_choice == 2) :
        introduction() 
        # display_menu()
        # not sure if this is what goes here but it is a placeholder for now
    else :
        print("Thank you for playing!")
        bContinue = False
