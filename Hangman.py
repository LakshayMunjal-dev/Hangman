
import random
wlist = ["this", "is", "the", "list", "of", "words"]
# This is the list of the words we can use in our Hangman Game


# This is our main function
def main():
    word = getw(wlist)
    play(word)
    while input("Want to play again? (Y/N) ").upper() == "Y":
        word = getw(wlist)
        play(word)


# This is our get word function to select a random word from our list
def getw(wlist):
    word = random.choice(wlist)
    return word.upper()


# The guessedl will contain all the letters guessed by the user so that it is not repeated
# The guessedw will contain all the words guessed by the user so that it is not repeated
# ntries will hold the no. of tries left

def play(word):
    word_completion = "⭕" * len(word)
    guessed = False
    guessedl = []
    guessedw = []
    ntries = 6
    print("\n \t \t \t Let's play Hangman! 🎮")
    print(hangman(ntries))
    print("\t \t \t", (word_completion))
    print("\n")
    while not guessed and ntries > 0:
        guess = input("\t\tGuess a letter or word(🔤): ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessedl:
                print("You've already tried", guess, "!")
            elif guess not in word:
                print("\n\t\t", guess, "isn't in the word ❌")
                ntries -= 1
                print("\n\t\tNo. of tries left => ", ntries)
                guessedl.append(guess)
            else:
                print("\n\t\tNice one,", guess, "is in the word! ✅")
                guessedl.append(guess)
                word_as_list = list(word_completion)
                replacement = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in replacement:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "⭕" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessedw:
                print("\n\t\tYou've already tried ", guess, "!")
            elif guess != word:
                print("\n\t\t", guess, "isn't the word! 🚫")
                ntries -= 1
                print("\n\t\tNo. of tries left => ", ntries)
                guessedw.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("\n\t\tInvalid input!")
        print(hangman(ntries))
        print("\t \t \t", word_completion)
        print("\n")
    if guessed:
        print("Good Job, you guessed the word! 🏆\n")
    else:
        print("I'm sorry, but you ran out of tries. The word was " +
              word + ". Maybe next time!\n")


# This is the function to display our Hangman
# The stages list will display the specific hangman according to the no. of wrong tries
def hangman(ntries):
    stages = ["""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
              """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
              """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
              """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
              """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
              """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
              """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                   """
              ]
    return stages[ntries]


# This is the calling of our main() function to execute the program
if __name__ == "__main__":
    main()
