import random
import pandas
from csv import writer
from time import sleep
import time

def saveScore(date,GameRounds,GameLetters,Attempts):
    list = [date,GameRounds,GameLetters,Attempts]
    
    with open(r"highscores.csv", 'a') as file:
        FileData = writer(file)
        FileData.writerow(list)

class Dictionary:
    def DrawAWord(letters):
        Allwords = pandas.read_csv(r'dictionary.csv')
        SelectedWords = Allwords.loc[:,f"{letters} letters"]
        Word = random.choice(SelectedWords)
        return Word
    def selectword():
        if GameOptions.letters == 4:
            return Dictionary.DrawAWord(4)
        elif GameOptions.letters == 5:
            return Dictionary.DrawAWord(5)
        elif GameOptions.letters == 6:
            return Dictionary.DrawAWord(6)
        else:
            print("An error occured. Please contact me!\n")

class Validator:
    def CheckIfIsogram(word):
        letter = set()
        return not any(i in letter or letter.add(i) for i in word)
          
class BullsAndCows:
    def __init__(self, bulls, cows):
        self.bulls = bulls
        self.cows = cows
    def printBullsAndCows(self):
        print(f"{self.bulls} Bulls, {self.cows} Cows")

class GameOptions:
    letters = 4
    rounds = 5
    def printOptions(self):
        if self.letters == 4 and self.rounds == 5:
            print(f"Default settings:\nWord lenght: {self.letters} letters\nRounds: {self.rounds}\n")
        else:
            print(f"Word lenght: {self.letters} letters\nRounds: {self.rounds}\n")
      
class Engine: 
    def returnBullsAndCows(CmpWord, UsrWord):
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
        Cword = Dictionary
        word = Cword.selectword()
        letters = GameOptions.letters
        rounds = GameOptions.rounds
        print(f"Computer has choosen a new word. This word has {letters} letters. Word {Validator.CheckIfIsogram(word)} isogram")
        while rounds > 0:
            print(f"Rounds left: {rounds}")
            user_word = input(f"Your guess ({letters} letters): ")
            user_word = user_word.upper()
            comp_word = word
            print(comp_word)
            if (len(user_word) == letters) and Validator.CheckIfIsogram(user_word):
                print(f"{Engine.returnBullsAndCows(comp_word, user_word)[0]} Bulls & {Engine.returnBullsAndCows(comp_word, user_word)[1]} Cows!")
                if Engine.returnBullsAndCows(comp_word, user_word)[0] == letters:
                    print("\n\nCongratulations, YOU WON THE GAME!\n")
                    sleep(1)
                    print("Going back to the Menu and saving your score\n")
                    saveScore(time.strftime("%b %d, %Y %H:%M"),GameOptions.rounds,GameOptions.letters,(rounds-GameOptions.rounds)*(-1))
                    sleep(1)
                    break
                elif Engine.returnBullsAndCows(comp_word, user_word)[0] == 0 and Engine.returnBullsAndCows(comp_word, user_word)[1] == 0:
                    print("These letters do not appear in the word. Try again!\n")
            else:
                print(f"\nWrite a word that has {letters} different letters!\n")
            rounds -= 1
            if (rounds - 1) == 0:
                print("\n----Your last chance!----\n")
            if rounds == 0:
                print("\n\n----Game Over!----\nTry again!\n")
                sleep(1)
                break
            
            
