import sys
import random
from utils.game import Hangman
import streamlit as st

game = Hangman()

def main(): 
    st.title("Sayı Tahmin Oyunu")
    """
    Organizes and run the game using the functions from Hangman class
    """
    while not game.game_over() and not game.well_played():
        game.start_game()
        letter = game.play()
        game.assess_guess(letter)
    return 
main()