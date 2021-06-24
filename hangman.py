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

    word_to_guess = ["january", "border", "image", "film",
                     "promise", "kids", "lungs", "doll",
                     "rhyme", "damage", "plants"]

    global word, length, count, display, already_guessed, play_game

    word = random.choice(word_to_guess)
    length, count, display, already_guessed, play_game = len(
        word), 0, "_"*len(word), [], ""


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


def hangman():

    global word, length, count, display, already_guessed, play_game

    limit = 5

    guess = input("This is the Hangman Word: " + display +
                  " Enter your guess: \n").strip()

    if len(guess) != 1:
        print("Invalid. Write a letter. \n")

    elif guess in word:

        already_guessed.extend([guess])
        index = word.find(guess)

        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]

        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter. \n")

    if word == '_'*length:
        print("Well done! You win!! \n")
        time.sleep(1)
        play_loop()
    elif count != limit:
        hangman()


main()
hangman()
#check play_loop

