def get_word():
    theword = input("Choose the word: ")
    print(f"The word you chose is: {theword}")
    return theword

def get_lives():
    number_of_lives = int(input("Choose the number of lives: "))
    return number_of_lives

def get_guess(suggested_letter):
    letter = input("Make a guess of a letter: ")
    
    while True:
        if letter in suggested_letter:
            letter = input("You've already made this guess, Try another: ")
        elif len(letter) != 1:
            letter = input("You guess should be a single letter: ")
        else: 
            break
    return letter 

def assess_guess(secret_word,guessed_letter,lives_left):
    secret_word = theword
    guessed_letter = suggested_letter[-1]
    lives_left = lives_left

    if guessed_letter in secret_word:
        lives_left = lives_left
        print (f"Correct!, you still have {lives_left} lives")
    else:
        lives_left = lives_left - 1
        print (f"Missed!, now you have {lives_left} lives") 
    return 

def display_word(secret_word, suggested_letters):
    secret_word = theword
    suggested_letters = suggested_letters
    display = ",".join("_" for i in range(len(theword)))
    print (display)
    return True if display == theword else False