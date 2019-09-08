import random

spaceman_winner_string = """
(\_/)
(0_0)
(u u)
(u u)
(u u)
"""
spaceman_loser_string = """
(\_/)
(X_X)
(u u)
(u u)
(u u)

"""
spaceman_loser_list = spaceman_loser_string.split('\n')
body_part_count = len(spaceman_loser_list)


def main():
    # sets up  list of themed words
    secret_string = random.choice(['eevee', 'mareep', 'pikachu'])
    secret_word = list(secret_string)
    secret_set = (secret_word)
    # game setup
    displayed_word_list = list("_" * len(secret_word))
    turns_remaining = body_part_count
    guess_history_string = ""
