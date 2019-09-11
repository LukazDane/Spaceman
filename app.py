# https://www.pythonforbeginners.com/
# https://stackoverflow.com/questions/22677853/python-import-text-file-as-list-to-iterate
# https://www.stechies.com/python-print-without-newline/
# Sh0ut 0ut to Audi for fixing my stupid stupid counter!!! Truely he is the MVP!
from collections import Counter
import random
# -----------------------------------
# for pokemon Spaceman -------------
# -----------------------------------
# f = open('pokemon.txt', 'r')
# words = f.readlines()
# f.close()
# print("Who's that Pokemon?")
# pokemon file currently contians capital letters, fix for later
# -----------------------------------

# for standard Spaceman
# -----------------------------------
f = open('words.txt', 'r')
words = f.readlines()
f.close()
print("Can you guess this word?")
# -----------------------------------
# comment this line out if you use a words.txt file with each word on a new line
words = words[0].split(' ')
letters_correct = []
letters_wrong = []
guesses = 0
count_correct = 0


def get_word():
    return random.randint(0, len(words) - 1)
# selects random word


def get_guess():
    for letter in word_letters:
        if (letter in letters_correct):
            print(letter, end="")
# prints correctly guessed letters in correct places
        else:
            print("_", end="")
    return input("\n\nGuess: ").lower()


word = get_word()
word_letters = list(words[word])
# print("This pokemon's name is " + str(len(words[word])) + " letters long.")
print("This word is " + str(len(words[word])) + " letters long.")

# print("---" + (words[word]) + "---")  # displays word for testing, delete later

while True:
    guess = get_guess()
    # print("---" + (words[word]) + "---")
    if guess.isalpha() and len(guess) < 2:
        if(guess in letters_correct) or (guess in letters_wrong):
            print("You already guessed " + guess + ". Try again...")
            # print(len(letters_correct))

        elif (guess in words[word]):
            letters_correct.append(guess)
            # global count_correct
            count_correct = 0
            for i in word_letters:
                if i in letters_correct:
                    count_correct += 1

            print("Correctly guessed: " + ", ".join(letters_correct))
            print("Incorrectly guessed: " + ", ".join(letters_wrong))
            print(str(guesses) + " of 7 lives lost!")
            # print(count_correct)
            # print(len(word_letters))

            if count_correct == len(words[word]):
                print(" You got it!\n It's " + words[word] + "\n")
                print("""
                \:.             .:/
                 \``._________.''/ 
                  \             / 
          .--.--, / .':.   .':. \
         /__:  /  | '::' . '::' |
            / /   |`.   ._.   .'|
           / /    |.'         '.|
          /___-_-,|.\  \   /  /.|
               // |''\.;   ;,/ '|
               `==|:=         =:|
                   `.          .'
                    :-._____.-:
                    `''       `''
          """)
                break
        else:
            letters_wrong.append(guess)
            print("Correctly guessed: " + ", ".join(letters_correct))
            print("Incorrectly guessed: " + ", ".join(letters_wrong))
            guesses += 1
            # print(*letters_wrong, sep=", ")
            print(str(guesses) + " of 7 lives lost!")
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

            elif guesses == 6:
                print("The pokemon is running away... Last Chance!")

            else:
                print("Looks like you need to go back to the trainer school...")
                print("It was... " + words[word])
                break

    else:
        if guess is not guess.isalpha():
            print("There's a time and place for everything. Please type a letter...")
            pass
