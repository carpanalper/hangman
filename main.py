import sys
import random
from utils.game import Hangman

game = Hangman()

def main(): 
    """
    Organizes and run the game using the functions from Hangman class
    """
    while not game.game_over() and not game.well_played():
        game.start_game()
        letter = game.play()
        game.assess_guess(letter)
    return 
main()