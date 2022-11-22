import random
from time import sleep


class Dictionary:
    def selectword():
        with open(r'projekt python\projektmain\dictionary.txt', 'r') as file:
            words = file.readlines()
            word = random.choice(words)
            return word

class Validator:
    def CheckIfIsogram():
        word = Dictionary.selectword()
        letter = set()
        return not any(i in letter or letter.add(i) for i in word)
    def CheckUserIsogram(user_word):
        letter = set()
        return not any(i in letter or letter.add(i) for i in user_word)
        
    
    
class BullsAndCows:
    def __init__(self, bulls, cows):
        self.bulls = bulls
        self.cows = cows
    def printBullsAndCows(self):
        print(f"{self.bulls} Bulls, {self.cows} Cows")


class GameOptions:
    def __init__(self, letters = 4, rounds = 5):
        self.letters = letters
        self.rounds = rounds
    def printOptions(self):
        if self.letters == 4 and self.rounds == 5:
            print(f"Default settings:\nLiczba liter: {self.letters}\nRounds: {self.rounds}")
        else:
            print(f"Letters: {self.letters}\nRounds: {self.rounds}")
    def printRounds(self):
        print(f"{self.rounds}")
    def getRounds(self):
        return self.rounds
    def printLetters(self):
        print(f"{self.letters}")
    def getLetters(self):
        return self.letters

        
class Engine:
    letterNum = GameOptions()
    letters = letterNum.getLetters()
    rounds = letterNum.getRounds()
    Cword = Dictionary
    word = Cword.selectword()
    def __init__(self):
        print("in init")
    
    def returnBullsAndCows(CmpWord, UsrWord):
        # print(f"{CmpWord} & {UsrWord}")
        comp = list(CmpWord)
        user = list(UsrWord)
        bullscows = BullsAndCows(0,0)
        for userIndex, CompIndex in zip(user, comp):
            if userIndex in comp:
                if userIndex == CompIndex:
                    bullscows.bulls += 1
                else:
                    bullscows.cows += 1

        return bullscows.bulls, bullscows.cows
                
    
    def gameEngine(self):
        print(f"Computer has choosen a new word. This word has {self.letters} letters. Word {Validator.CheckIfIsogram()} isogram")
        while self.rounds > 0:
            print(f"Rounds left: {self.rounds}")
            self.rounds -= 1
            user_word = input(f"Your guess ({self.letters} letters): ")
            user_word = user_word.upper()
            comp_word = self.word
            print(comp_word)
            if (len(user_word) == self.letters) and Validator.CheckUserIsogram(user_word):
                print(f"{Engine.returnBullsAndCows(comp_word, user_word)[0]} Bulls & {Engine.returnBullsAndCows(comp_word, user_word)[1]} Cows!")
                if Engine.returnBullsAndCows(comp_word, user_word)[0] == 4:
                    print("You won the game !!!!!!!")
                    sleep(1)
                    print("Goin back to the menu")
                    sleep(1)
                    break
                elif Engine.returnBullsAndCows(comp_word, user_word)[0] == 0 and Engine.returnBullsAndCows(comp_word, user_word)[1] == 0:
                    print("Your guess has not been right. Try again! You")
            elif self.rounds == 0:
                break    
            else:
                print(f"Write a word that has {self.letters} different letters!")
            
        
        
    


