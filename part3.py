#Porter Collins
#This function lets you choose two teams and returns the two teams in a list. Home team first opponent second.

def pick_teams(Not_Necessary = None) :
    lstDisplayTeams = ["1 - BYU", "2 - USU", "3 - Texas Tech", "4 - OSU", "5 - University of Utah"]
    lstUsableTeams = ["BYU", "USU", "Texas Tech", "OSU", "University of Utah"]
    lstTeams = []

    #This loop is how they choose their home team.
    while True :
        print("\n---Teams to choose from---")
        print(lstDisplayTeams[0])
        print(lstDisplayTeams[1])
        print(lstDisplayTeams[2])
        print(lstDisplayTeams[3])
        print(lstDisplayTeams[4]) 
        try :
            iChoice = int( input("\nPlease select your team: "))

            if (iChoice == 1 or iChoice == 2 or iChoice == 3 or iChoice == 4 or iChoice ==5) :
                lstTeams.append(lstUsableTeams[iChoice - 1])
                break

            else :
                print("Invalid response. Please enter a valid response (i.e. 1-5).")

        except :
            print("Invalid response. Please enter a valid response (i.e. 1-5).")

    lstDisplayTeams.pop(iChoice - 1) 

    #This is how they choose their opponent
    while True :
        print("\n---Teams to choose from---")
        print(lstDisplayTeams[0])
        print(lstDisplayTeams[1])
        print(lstDisplayTeams[2])
        print(lstDisplayTeams[3]) 

        try :
            iChoice2 = int( input("\nPlease select the opposing team: "))

            if ((iChoice2 == 1 or iChoice2 == 2 or iChoice2 == 3 or iChoice2 == 4 or iChoice2 == 5) and iChoice2 != iChoice) :
                lstTeams.append(lstUsableTeams[iChoice2 - 1])
                break

            else :
                print("Invalid response. Please enter a valid response (i.e. 1-5) (Also it can't be the same number you chose last time).")

        except :
            print("Invalid response. Please enter a valid response (i.e. 1-5).")

    #This returns the two teams in a list the Home team first and the opponent second.
    return lstTeams

        


