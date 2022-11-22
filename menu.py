from time import sleep
import classes

def valueerror():
    print("\n-----Enter a number, for example 2-----\n")
    sleep(2)
def userinput():
    user_input = int(input("Enter the number representing the selected option: "))
    print()
    return user_input
print("Welcome to the Bulls & Cows game!")

while True:
    print("\
    Menu:\n\
    1. New game\n\
    2. Game rules\n\
    3. Game options\n\
    4. Exit game")
    
    try:
        user_action = userinput()
        
        if user_action == 1:
            print("\n\n\nNew Game\n\n\n")
            sleep(1)
            opcje = classes.GameOptions()
            NewGame = classes.Engine()
            opcje.printOptions()
            NewGame.gameEngine()
                
        elif user_action == 2:
            with open(r'projekt python\projektmain\rules.txt', 'r') as file:
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
                                opcje.letters = 4
                            elif user_lenght_action == 2:
                                opcje.letters = 5
                            elif user_lenght_action == 3:
                                opcje.letters = 6
                        except ValueError:
                            valueerror()
                            continue
                    elif user_Options_action == 2:
                        try:
                            print("1. 5 rounds (default)\n2. 8 rounds\n3. 12 rounds\n")
                            user_round_action = userinput()
                            if user_round_action == 1:
                                opcje.rounds = 5
                            elif user_round_action == 2:
                                opcje.rounds = 8
                            elif user_round_action == 3:
                                opcje.rounds = 12
                        except ValueError:
                            valueerror()
                            continue
                    elif user_Options_action == 3:
                        break
                except ValueError:
                    valueerror()
                    continue
        
                                
        elif user_action == 4:
            print("Thank you for the game. See ya!")
            sleep(2)
            exit()

            
        else:
            print("\n----Wpisz cyfre od 1 do 4----\n")
            
    except ValueError:
        valueerror()
        continue