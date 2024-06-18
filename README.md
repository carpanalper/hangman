### CARD HANGMAN

## Introduction

**Hangman** is a well-known game which players try to guess a word letter by letter. 
Each turn the player makes a guess and if the secret word contains the guessed letter, then the game operator reveals the position of the correctly guessed letters. If not the operator starts drawing a body part of a man who is meant to be hanged after too many wrong guesses. 
**The goal** is guessing all the letters correctly before running out of the lives and saving the man from getting hanged.

In our game the player has 5 lives. It means you can only make 4 wrong guesses before the game is over. 

## Features

**Getting Unique Guesses:** The program ask for a letter from the player and only continue if the player provides a single letter which is different from previous guesses. 

**Displaying Game Status** The program displays a series of underscores which has the same length with the secret word. It reveals the letters as the player make good guesses and counts the turn and errors. 

**Making a List of Wrong Guesses** The program also makes the list of wrong guesses and displays it on the each turn to prevent player the make same mistakes repeatedly. 

**Ending the Game** Program ends the game if the player make 5 wrong guesses or guesses the word correctly before running out of lives.

## File Structure 

`main.py`: Main script to execute the program\
`utils/game.py`: Contains functions to operate the game, to ensure smooth flow of thee game under the class "Hangman"\
`draft/draft.py`: Contains experimental functions for the preperation for coding game.py. 

## Installation & Usage

1. Clone the repository: 

```bash
    git clone https://github.com/carpanalper/hangman
    cd hangman
```

2. Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

3. Run the mainscript 

```bash
    python main.py 
```
4. Provide a single different letter on each turn until the game is over and Follow the on-screen instructions. To play again run the mainscript again after the session.

## Contributors

Alper Carpan

