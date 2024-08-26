#datetime is imported to control the exact date whenever a game is saved
from datetime import date
#Controls the CPU side of the game to allow the bot to place an "O" on the board at random
import random
#We will set this up later


date_of_game = date.today()
#initializes wins and losses to be zero until the player wins or loses a game
wins = 0
player_losses = 0
#initializes the first option as "X" before the turn is switched to "O"
currentoption = "X"
#declaredwinner is set to None before it is changed to "X" or "O" in the game win logic
declaredwinner = None
#Player name is initialized to None before the player changes it
player_name = None
#Game is running until the player wins a game, loses a game, or ends up in a tie
gameisrunning = True


#initializes the info dictionary, which controls all info about the player
info = {}
#Initializes an empty array so that players can replace the dashed with an "X" or an "O" string
tictacboard = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#sets up gameboard
def gameboard(tictacboard):
    print(str(tictacboard[0]) + " | " + str(tictacboard[1]) + " | " + str(tictacboard[2]))
    print("---------")
    print(str(tictacboard[3]) + " | " + str(tictacboard[4]) + " | " + str(tictacboard[5]))
    print("---------")
    print(str(tictacboard[6]) + " | " + str(tictacboard[7]) + " | " + str(tictacboard[8]))

#Gives user a choice of numbers 1-9 to select from the gameboard, and it subtracts from player input to match the list index
def play(tictacboard):
    try:
        choice = int(input("Select a number (1-9): "))
        if choice >= 1 and choice <= 9 and tictacboard[choice-1] == "-":
            tictacboard[choice-1] = currentoption
        elif tictacboard[choice-1] != "-":
            print("This spot on the board has already been chosen. Try another one.")
    except ValueError:
        print("The value you entered is not acceptable. Make sure you are only inputing an integer.")

#Checks for a winner in the horizontal left-right direction
def horziontal(tictacboard, c):
    global declaredwinner
    if tictacboard[0] == tictacboard[1] == tictacboard[2] and tictacboard[1] != "-" and tictacboard[0] == c:
        declaredwinner = tictacboard[0]
        return True
    elif tictacboard[3] == tictacboard[4] == tictacboard[5] and tictacboard[4] !=  "-" and tictacboard[3] == c:
        declaredwinner = tictacboard[3]
        return True
    elif tictacboard[6] == tictacboard[7] == tictacboard[8] and tictacboard[7] != "-" and tictacboard[6] == c:
        declaredwinner = tictacboard[6]
        return True
    return False
#Checks for a winner in the vertical up-down direction
def vertical(tictacboard, c):
    global declaredwinner
    if tictacboard[0] == tictacboard[3] == tictacboard[6] and tictacboard[3] != "-" and tictacboard[0] == c:
        declaredwinner = tictacboard[0]
        return True
    elif tictacboard[1] == tictacboard[4] == tictacboard[7] and tictacboard[4] != "-" and tictacboard[1] == c:
        declaredwinner = tictacboard[1]
        return True
    elif tictacboard[2] == tictacboard[5] == tictacboard[8] and tictacboard[5] != "-" and tictacboard[2] == c:
        declaredwinner = tictacboard[2]
        return True
    return False
#Checks if there is a win in any direction of diagonals
def diagonal(tictacboard, c):
    global declaredwinner
    if tictacboard[2] == tictacboard[4] == tictacboard[6] and tictacboard[4] != "-" and tictacboard[2] == c:
        declaredwinner = tictacboard[2]
        return True
    
    elif tictacboard[0] == tictacboard[4] == tictacboard[8] and tictacboard[4] != "-" and tictacboard[0] == c:
        declaredwinner = tictacboard[0]
        return True
    return False

##Checks to see if there was a tie game between the computer and the player
def checkfortiefunction(tictacboard):
    if "-" not in tictacboard and not checkforagamewin():
        print("Game is tied!")
        gameboard(tictacboard)
        return True
    return False

##Checks to see if the player wins the game
def checkforagamewin():
    global gameisrunning
    
    if horziontal(tictacboard, "X") or vertical(tictacboard, "X") or diagonal(tictacboard, "X") or horziontal(tictacboard, "O") or vertical(tictacboard, "O") or diagonal(tictacboard, "O"):
        if declaredwinner == "X":
            winner_name = player_name
            print(f"{winner_name} has won BCCA Tic-Tac-Toe!")
            info[player_name]['Wins'] += 1
            
            
            
        elif declaredwinner == "O":
            winner_name = "The CPU"
            print(f"{winner_name} has won BCCA Tic-Tac-Toe!")
            info[player_name]['Losses'] += 1
            


        
        gameboard(tictacboard)
        return True
    return False

#Manages the switch from X to O on the gameboard
def switchingXtoO():
    global currentoption
    if currentoption == "X":
        currentoption = "O"
    else:
        currentoption = "X"
#All information about how the CPU behaves (Uses the random import to select numbers 0-8 on the board)
def cpuaction(tictacboard):
    while currentoption == "O":
        cpu_on_board = random.randint(0,8)
        if tictacboard[cpu_on_board] == "-":
            tictacboard[cpu_on_board] = "O"
            switchingXtoO()
#Uses player info like name, wins, and losses, as well as the date the game was played and saves it to a file
def savegametofile():
    with open('gamesave.txt', 'w') as saveddata:
            saveddata.write(f"""
    ----------------------------
    Date of Game: {date_of_game}
    Player Name: {player_name}
    Wins: {info[player_name]['Wins']}
    Losses: {info[player_name]['Losses']}
    ----------------------------
    """)
     
    print("Saving game data to file... ")
    
def main():
    print("""Welcome to Base Camp Coding Academy Tic-Tac-Toe.
------------------------------------------------
            Version 1.0 | CPU vs Player""")
                                                                    
    global player_name
    if player_name == None:
                
            
        player_name = input("Enter your name: ")
        if player_name:
            info[player_name] = {'Wins': 0, 'Losses': 0}
                    
        else:
            print("Invalid input! ")
    
    while True:
        
        option = input("""
Please Choose a Number 1-5:
---------------------
1. Play Tic-Tac-Toe
2. View Controls
3. Save an existing game of Tic-Tac-Toe
4. View Game Statistics
5. Quit Tic-Tac-Toe
Select an option: """)
        
        global tictacboard
        tictacboard = ["-","-","-",
         "-","-","-",
         "-","-","-"]
        if option == "1":
            gameisrunning= True
            
            
            
            
                
            while gameisrunning:
                
                gameboard(tictacboard)
                play(tictacboard)
                if checkforagamewin():
                    gameisrunning = False
                    break
                if checkfortiefunction(tictacboard):
                    gameisrunning = False
                    break
                
                switchingXtoO()
                cpuaction(tictacboard)
                if checkforagamewin():
                    gameisrunning = False
                    break
                if checkfortiefunction(tictacboard):
                    gameisrunning = False
                    break
                
        elif option == "2":
            print("""
Here are the numbered locations for the Tic-Tac-Board:
                  1 | 2 | 3
                  ---------
                  4 | 5 | 6
                  ---------
                  7 | 8 | 9
""")
            

        elif option == "3":
            savegametofile()
        elif option == "4":
            print(f"""
        Player Name: {player_name}
        Wins: {info[player_name]['Wins']}
        Losses: {info[player_name]['Losses']}
                """)
            


        elif option == "5":
            print("Exiting game... ")
            break
            
        else:
            print("Invalid input. Please choose from 1-4.")

if __name__ == "__main__":
    main()
