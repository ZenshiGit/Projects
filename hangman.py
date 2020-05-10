import os
import random
import time

print("\n -----------------------------------------------------------")
print("|                         HANGMAN                           |")
print(" -----------------------------------------------------------")

print("\n1. Play")
print("2. Exit")

m1 = " "
m2 = " "
m3 = " "
m4 = " "
m5 = " "
m6 = " "
mistake_no = 0

word_list = ["approach", "argue", "board", "building", "challenge", "environment", "field", "heavy", "international", "language", "memory", "network", "organization", "phone", "radio", "science", "technology", "window"]
word = random.choice(word_list).upper()
word_game = "_ " * len(word)
wrong_letter = False
cls = lambda: os.system("cls")

def hangman():
    print("\n")
    print("      _________")
    print("     |       ", m1)
    print("     |     ", m3, m2, m4)
    print("     |      ", m5, m6)
    print("     |")
    print("     |                       ", word_game)
    print("  _______")

def mistakes(mistake_no):
    global m1, m2, m3, m4, m5, m6
    if mistake_no == 1:
        m1 = "0"
    elif mistake_no == 2:
        m2 = "|"
    elif mistake_no == 3:
        m3 = "/"
    elif mistake_no == 4:
        m4 = "\\"
    elif mistake_no == 5:
        m5 = "/"
    else:
        m6 = "\\"

def game_won():
    print(" ------------------------------------")
    print("|      Congratulations! You win!     |")
    print(" ------------------------------------")

def game_lost():
    print(" ------------------------------------ ")
    print("|              You lose!             |")
    print(" ------------------------------------")

choice = int(input("\nType 1 or 2, then hit Enter: "))

while choice != 1 and choice != 2:
    print("Invalid value!")
    choice = int(input("\nType 1 or 2, then hit Enter: "))

if choice == 2:
    print("")
else:
    cls()
    hangman()
    while "_" in word_game and mistake_no < 6:
        wrong_letter = True
        letter = input("\nType a letter, then hit Enter: ").upper()
        while len(letter) > 1 or letter.isalpha() == False or letter.upper() in word_game:
            if letter.upper() in word_game:
                print("The letter is already in the word.")
            else:
                print("Invalid value!")
            time.sleep(2)
            cls()
            hangman()
            letter = input("\nType a letter, then hit Enter: ")
        for x in range(len(word)):
            if word[x] == letter:
                word_game = word_game[:x * 2] + letter + word_game[x * 2 + 1:]
                wrong_letter = False
                cls()
                hangman()
        if wrong_letter == True:
            mistake_no += 1
            mistakes(mistake_no)
            cls()
            hangman()
    if mistake_no >= 6:
        cls()
        word_game = ""
        hangman()
        game_lost()
        time.sleep(2)
    else:
        cls()
        print("\n           ", word_game, "\n")
        game_won()
        time.sleep(2)

cls()
print("\nThe window will close in...")
for z in range(3, 0, -1):
    print(z)
    time.sleep(0.9)