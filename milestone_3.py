
import random

# While loop that cheks if the guesssed character is in the word 

def check_guess():
    guess = 0

    while True:
        guess = input("Guess a letter: ")

        if len(guess) == 1 and guess.isalpha():
            print("Well done! You guessed:", guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")



# Using my random word list of fruits from my file milestone_2.py

word_list = ["apple", "orange", "kiwi", "mango", "cherry"]

# Using pythons random function to select a random letter from the word list 

secret_word = random.choice(word_list)

# Creating a while loop that checks if the user is able to guess a letter in the secret word from my list selected by the computer 

def ask_for_input():

    guess = 0

    while True:
        guess = input("Guess a letter: ")

        if len(guess) == 1 and guess.isalpha():
            if guess in secret_word:
                print(f"Good guess! '{guess}' is in the word.")
            else:
                print(f"Sorry, '{guess}' is not in the word. Try again.")
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

check_guess()

ask_for_input()