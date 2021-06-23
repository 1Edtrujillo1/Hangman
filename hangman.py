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

# start game


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

    global word
    global already_guessed
    global display
    global count

    guess = input("This is the Hangman Word: " + display +
                  " Enter your guess: \n").strip()

    if guess in word:

        already_guessed.extend([guess])
        index = word.find(guess)

        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]

    elif guess in already_guessed:
        print("Try another letter.")

    elif len(guess != 1):
        print("Try a letter \n")
        hangman()

    else:
        limit = 5

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

            print("Wrong guess. " + str(limit - count) + "guesses remain.")

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

            print("Wrong guess. " + str(limit - count) + "guesses remain.")

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

            print("Wrong guess. " + str(limit - count) + "guesses remain.")

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

            print("Wrong guess. " + str(limit - count) + "last guess remain,")

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

            print("Wrong guess. You are hanged" +
                  "\n Th word was:" + word)
            play_loop()

    if word == '_'*length:
        print("Congrats! You win")
        play_loop()
    elif count != limit:
        hangman()


main()
hangman()
