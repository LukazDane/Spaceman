import random

# test
words = ['eevee', "pikachu", "entei", "abra"]
letters_correct = []
letters_wrong = []
guesses = 0
word = get_word()
wordletters = list(words[word])

print("Who's that Pokemon?")


def get_word():
    return random.randint(0, len(words) - 1)


def get_guess():
    for letter in word_letters:
        if (letter in letters_correct):
            print(letter)
        else:
            print("_")

    return input("\n\nGuess: ")


while True:
    guess = get_guess()
    if(guess in words[word]):
        letters_correct.append(guess)
        print("You got it!")

        if(len(letters_correct) == len(words[word])):
            print(" You got it!\n\n It's " + words[word] + "\n\n")
            break

    else:
        letters_wrong.append(guess)
        if guesses == 0:

            print("  !  ")
            print("(\_/)")
        elif guesses == 1:
            print("  |  ")
            print("  .  ")
            print("(\_/)")
        elif guesses == 2:
            print("  |  ")
            print("  |  ")
            print("  O  ")
            print("(\_/)")
        elif guesses == 3:
            print(" |‾| ")
            print(" | | ")
            print(" |_| ")
            print("  O  ")
            print("(\_/)")
        elif guesses == 4:
            print(" /‾/ ")
            print(" \_\ ")
            print(" /_/ ")
            print("  O  ")
            print("(\_/)")
        elif guesses == 5:
            print(" -_  ")
            print(" __- ")
            print("    ‾")
            print("    ‾")
            print("-‾‾-_")
        else:
            print("The pokemon ran away...")

if (len(letters_correct) == 7):
    print("Looks like you need to go back to the trainer school...")
    print("It was... " + words[word])
