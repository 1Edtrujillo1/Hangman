# 0.0 Import modules ----

import random
import time


# 1.0 Starting the game ----


# 1.0 Functions with specific global arguments ----

# 2.0 Loops to execute the program ----

# 3.0 Run program passing the function ----

# define global variables for the game.
def main():

    print("Welcome to Hangman game!")
    time.sleep(3)
    name = input("Enter your name: ")
    print("\n Hello " + name + "\n The game is about to start." + "\n Good Luck!")
    time.sleep(2)

    global word
    global length
    global count
    global display
    global already_guessed
    global play_game

    word_to_guess = ["january", "border", "image", "film",
                     "promise", "kids", "lungs", "doll",
                     "rhyme", "damage", "plants"]

    word = random.choice(word_to_guess)
    length = len(word)
    count = 0
    display = "_"*length
    already_guessed = []
    play_game = ""


def play_loop():

    global play_game

    play_game = input("Do You want to play again? y = yes, n = no \n")

    while play_game not in ["y", "Y", "n", "N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")

        if play_game == "y":
            main()
        elif play_game == "n":
            print("\n Thanks for Playing!" + "\n Never come back!" +
                  "\n Love You.")
            exit()


play_loop()

#main()
