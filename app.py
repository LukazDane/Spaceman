import random

# test
words = ['eevee', "pikachu", "entei", "abra"]
letters_correct = []
letters_wrong = []
guesses = 0


def get_word():
    return random.randint(0, len(words) - 1)


def get_guess():
