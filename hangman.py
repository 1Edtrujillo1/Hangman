# 0.0 Import modules ----

import random
import time
#import sys

# 1.0 Starting the game ----


# 1.0 Functions with specific global arguments ----

# 2.0 Loops to execute the program ----

# 3.0 Run program passing the function ----

# define global variables for the game.
def play_loop():

    play_game = input("Do You want to play? y = yes, n = no \n")

    while play_game not in ["y", "Y", "n", "N"]:
        play_game = input("Do You want to play? y = yes, n = no \n")

        if play_game == "y":

            time.sleep(1)
            main()
            time.sleep(2)
            hangman()
        elif play_game == "n":
            print("\n Never come back!" + "\n Love You.")
            exit()


def main():

    print("Welcome to Hangman game!")
    time.sleep(3)
    name = input("Enter your name: ")
    print("\n Hello " + name + "\n The game is about to start." + "\n Good Luck! \n")
    time.sleep(2)

    word_options = ["january", "border", "image", "film",
                    "promise", "kids", "lungs", "doll",
                    "rhyme", "damage", "plants"]

    global word, length, count, display, already_guessed, word_to_guess

    word = random.choice(word_options)
    length, count, display, already_guessed, word_to_guess = len(word), 0, \
        "_"*len(word), [], word


def hangman():

    global word, length, count, display, already_guessed, word_to_guess

    limit = 5

    guess = input("This is the Hangman Word: " + display +
                  " Enter your guess: \n").strip()

    if len(guess) != 1 or guess.isdigit():
        print("Invalid. Write a letter. \n")

    elif guess in word:

        already_guessed.extend([guess])
        index = word.find(guess)

        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]

        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter. \n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit-count) + " guesses remain. \n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit-count) + " guesses remain. \n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit-count) + " guesses remain. \n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit-count) + " last guess remain. \n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit-count) + "guesses remain. \n" +
                  "The word was: " + word_to_guess)
            time.sleep(1)
            play_loop()

    if word == '_'*length:
        print("Well done! You win!! \n")
        time.sleep(1)
        play_loop()

    elif count != limit:
        hangman()


#sys.modules[__name__].__dict__.clear()
play_loop()
