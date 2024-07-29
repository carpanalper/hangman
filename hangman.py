import random
import streamlit as st
from typing import List

class Hangman:
    """
    Hangman class inclues functions and variables to organize the flow of game "Hangman"
    """
    def __init__(self, lives: int = 5):
        self.possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions', 'python', 'fantastic', 'belgium']
        self.word_to_find: str = random.choice(self.possible_words)
        self.lives: int = lives
        self.correctly_guessed_letters: List[str] = ["_" for _ in range(len(self.word_to_find))]
        self.wrongly_guessed_letters: List[str] = []
        self.error_count: int = 0
        self.turn_count: int = 1

    def play(self, letter: str):
        """Processes a player's guess."""
        if letter in self.correctly_guessed_letters or letter in self.wrongly_guessed_letters:
            return False  # Already guessed
        if len(letter) != 1 or letter.isdigit():
            return False  # Invalid guess
        self.turn_count += 1
        return True  # Valid guess

    def assess_guess(self, letter: str):
        """Assesses if the guess is correct."""
        if letter not in self.word_to_find:
            self.wrongly_guessed_letters.append(letter)
            self.error_count += 1
            self.lives -= 1
        else:
            for i in range(len(self.word_to_find)):
                if self.word_to_find[i] == letter:
                    self.correctly_guessed_letters[i] = letter

    def start_game(self):
        """Displays the current state of the game."""
        return " ".join(self.correctly_guessed_letters), self.lives, self.error_count, self.wrongly_guessed_letters

    def game_over(self) -> bool:
        """Checks if the game is over."""
        return self.lives == 0

    def well_played(self) -> bool:
        """Checks if the player has guessed the word correctly."""
        return "_" not in self.correctly_guessed_letters

# Streamlit app
def main():
    st.title("Hangman")
    
    if 'game' not in st.session_state:
        st.session_state.game = Hangman()

    current_game = st.session_state.game
    current_state, lives, errors, wrong_guesses = current_game.start_game()

    st.write(f"Word: {current_state}")
    st.write(f"Lives: {lives}")
    st.write(f"Errors: {errors}")
    st.write(f"Missed: {wrong_guesses}")

    letter = st.text_input("Guess a letter:", max_chars=1)

    if st.button("Shoot"):
        if letter:
            if current_game.play(letter):
                current_game.assess_guess(letter)
                if current_game.well_played():
                    st.success(f"Congrats! You made it: '{current_game.word_to_find}'")
                    st.session_state.game = Hangman()  # Yeni oyuna başla
            else:
                st.warning("Already guessed or invalid guess.")
        else:
            st.warning("Guess a LETTER")

    if current_game.game_over():
        st.error(f"Game Over! The word was: '{current_game.word_to_find}' idi.")
        st.session_state.game = Hangman()  # Yeni oyuna başla

if __name__ == "__main__":
    main()
