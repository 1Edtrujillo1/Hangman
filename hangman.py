# 0.0 Import modules ----
import random
import time


# 1.0  Define necessary functions ----

def play_loop():
    """When this function is run, the game will start iteratively.
        Returns:
        Iterative game until the user stop it.
    """

    play_game = ""

    input("Do You want to play?\n")

    while play_game not in ["y", "Y", "n", "N"]:

        play_game = input("y = yes, n = no \n")

        if play_game == "y":
            time.sleep(1)
            main()
            time.sleep(2)
            hangman()
        elif play_game == "n":
            print("\n Never come back!" + "\n Love You.")
            exit()


def main():
    """Define the starting necessary variables to play the game.
        Returns:
        Global Variables
    """

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
    """When this function is runned the user will play the hangman game.
        Returns:
        An interactive hangman game
    """

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

        counted = list(range(6))[1:]
        incorrect = [("   _____ \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n"),
                     ("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n"),
                     ("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n"),
                     ("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n"),
                     ("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |    /|\ \n"
                      "  |    / \ \n"
                      "__|__\n")]

        incorrect_message = ["Wrong guess. " + str(limit-count) +
                             " guesses remain. \n" for i in range(len(counted))]
        incorrect_message[-1] = incorrect_message[-1] + \
            "The word was: " + word_to_guess

        if count in counted:
            time.sleep(1)
            print({counted[i]: incorrect[i]
                  for i in range(len(counted))}[count])
            print({counted[i]: incorrect_message[i]
                  for i in range(len(counted))}[count])

        if count == 5:
            play_loop()

    if word == '_'*length:
        print("Well done! You win!! \n")
        time.sleep(1)
        play_loop()

    elif count != limit:
        hangman()


# 2.0 Play the game ----
play_loop()
