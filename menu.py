from time import sleep
import classes
import pandas

def valueerror():
    print("\n-----Enter a number, for example 2-----\n")
    sleep(2)
    
def userinput():
    user_input = int(input("Enter the number representing the selected option: "))
    print()
    return user_input
print("Welcome to the Bulls & Cows game!\n")

opcje = classes.GameOptions()
new_game = classes.Engine()
while True:
    print("\
    Menu:\n\
    1. New game\n\
    2. Game rules\n\
    3. Game options\n\
    4. Scores\n\
    5. Exit game")
    
    try:
        user_action = userinput()
        if user_action == 1:
            print("\n\n\nNew Game\n\n\n")
            sleep(1)
            new_game.gameEngine()
            opcje.printOptions()     
        elif user_action == 2:
            with open(r'rules.txt', 'r') as file:
                print(file.read())
        elif user_action == 3:
            while True:
                sleep(1)
                print("\n\n----Menu/Game settings----\n")
                opcje.printOptions()
                try:
                    print("1. Change word lenght\n2. Change the number of rounds\n3. Back to menu\n")
                    user_Options_action = userinput()
                    if user_Options_action == 1:
                        try:
                            print("1. 4 letters (default)\n2. 5 letters\n3. 6 letters\n")
                            user_lenght_action = userinput()
                            if user_lenght_action == 1:
                                classes.GameOptions.letters = 4
                            elif user_lenght_action == 2:
                                classes.GameOptions.letters = 5
                            elif user_lenght_action == 3:
                                classes.GameOptions.letters = 6
                        except ValueError:
                            valueerror()
                            continue
                    elif user_Options_action == 2:
                        try:
                            print("1. 5 rounds (default)\n2. 8 rounds\n3. 12 rounds\n")
                            user_round_action = userinput()
                            if user_round_action == 1:
                               classes.GameOptions.rounds = 5
                            elif user_round_action == 2:
                                classes.GameOptions.rounds = 8
                            elif user_round_action == 3:
                                classes.GameOptions.rounds = 12
                        except ValueError:
                            valueerror()
                            continue
                    elif user_Options_action == 3:
                        break
                except ValueError:
                    valueerror()
                    continue
        elif user_action == 4:
            df = pandas.read_csv(r"highscores.csv", names=("Date","GameRounds","GameLetters","Attempts"))
            df = df[df.groupby(['GameLetters'])['Attempts'].transform(min) == df['Attempts']]
            df.reset_index(drop=True, inplace=True)
            print(f"{df}")
                                      
        elif user_action == 5:
            print("Thank you for the game. See ya!")
            sleep(2)
            exit()
        else:
            print("\n----Wpisz cyfre od 1 do 4----\n")
    except ValueError:
        valueerror()
        continue
