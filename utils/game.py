import random
from typing import List

class Hangman:
    """
    Hangman class inclues functions and variables to organize the flow of game "Hangman"

        Attributes: 
            possible_words (List) : a list of words for a user to guess
            word_to_find (string) : this word is chosen randomly from possible_words and expected to be guessed during the session
            lives (int) : the maximum number of mistakes can a user make during a session. It is 5 as defualt.
            correctly_guessed_letters (List) : It is the list of underscores as long as the word_to_find. As the user guess correctly 
        underscore replaced by the letters at the same spot.
            wrongly_guessed_letters (List): a list collects the wrong guesses of the user during the session.
            error_count (int): counts wrong guesses during a game session
            turn_count (int): counts turns as guesses are made

    """
    def __init__(self, lives:int = 5):
            self.possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions']
            self.word_to_find: str = random.choice(self.possible_words)
            self.lives: int = lives
            self.correctly_guessed_letters: List[str] = ["_" for i in range(len(self.word_to_find))]
            self.wrongly_guessed_letters: List[str] = []
            self.error_count: int = 0
            self.turn_count: int = 1

    def __str__(self):
        return print (f"Lives:{self.lives}, Turn{self.turn_count}, Errors: {self.error_count}")

    def play(self):
        
        """
        Gets a guess as long as it is only a single letter
        Check if the guess made before
        Warns the user accordingly
        Counts the turns
        Check if the guess is correct or not 
        """

        letter: str = input("Make a guess of a letter: ")
        while True:
            if letter in self.correctly_guessed_letters or letter in self.wrongly_guessed_letters:
                letter = input("You've already made this guess, Try another: ")
            elif len(letter) != 1 or letter.isdigit():
                letter = input("You guess should be a single letter: ")
            else:
                self.turn_count += 1 
                break
            return 

        if letter not in self.word_to_find:
            self.wrongly_guessed_letters.append(letter)
            self.error_count += 1   
            self.lives -= 1
            print (f"Missed!, now you have {self.lives} lives")
        else:
            for i in range(len(self.word_to_find)):
                if self.word_to_find[i] == letter:
                    self.correctly_guessed_letters[i] = letter   
            print (f"Correct!, you still have {self.lives} lives") 
        return  
    
    def start_game(self):
        """
        Displays the current state of game as revaling word_to_find, counts of turns and errors and lives as well as the list of wrong guesses.
        """
        print (" ".join(self.correctly_guessed_letters))
        print (f"Turn: {self.turn_count}, Error: {self.error_count}, Lives Left: {self.lives}")
        print (f"Missed:{self.wrongly_guessed_letters}")
        return
    
    def game_over(self) -> bool:
        """
        End the game if the user run out of lives
        """
        if self.lives == 0:
            print ("")
            print (f"Game Over! The word was '{self.word_to_find}'")
            print ("")
            return True
        else:   
            return False
    
    def well_played(self) -> bool:
        """
        End the game if the user correctly guess all the letters.
        """
        if "_" not in self.correctly_guessed_letters:
            print ("")
            print (f"You found the word: '{self.word_to_find}', in {self.turn_count} turns with {self.error_count} errors!")
            print ("")
            return True
        else:
            return False