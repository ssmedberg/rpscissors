"""
A simple program that will play rock-paper-scissors with you.

To run the program, type `python rpscissors.py`.
"""

import random

# This is a dictionary. The key is a 2-tuple e.g. ('rock', 'paper')
# the value is a boolean True/False to indicate whether player1 should win.
# NOTE: ties are *not* included in this map. They should be checked
# programmatically.

matchups = {
    ('rock', 'paper'): False,
    ('paper', 'rock'): True,
    ('rock', 'scissors'): True,
    ('scissors', 'rock'): False,
    ('paper', 'scissors'): False,
    ('scissors', 'paper'): True,
}

def get_result(play1, play2):
    """
    Return True if play1 beats play2, or False if not. Returns None if the
    plays tie.
    """

    if play1 == play2:
        return None

    return matchups[(play1, play2)]

def get_random():
    """
    Rolls a 3-way dice to pick a random play.
    """
    return random.choice(['rock', 'paper', 'scissors'])

print "Let's play rock-paper-scissors!"

user_play = raw_input("Type rock/paper/scissors: ")
computer_play = get_random()

print "I chose %s!" % (computer_play,)

result = get_result(user_play, computer_play)
if result is None:
    print "It's a tie"
elif result:
    print "You win!"
else:
    print "You lose."
