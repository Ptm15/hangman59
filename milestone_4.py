

import random

# Creating my list with my faveourute fruits 

word_list = ["apple", "orange", "kiwi", "mango", "cherry"]

# Creating my hangman class 

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))  # Count of unique letters
        self.list_of_guesses = []   

# Method and fucntion for checking if the guess is in the letter for the hangman game 

    def check_guess(self, guess):
            guess = guess.lower()  
            if guess in self.word:
                print(f"Good guess! '{guess}' is in the word.")

# Ending my method with a for loop that will replace the underscores in word_guessed with a letter

    def check_guess(self, guess):
        guess = guess.lower()  
        if guess in self.word:
            print(f"Good guess, '{guess}' is in the word!")

            # Loops through each letter of the word
            for i, letter in enumerate(self.word):
                if letter == guess:
                    # Replacing the underscore/_ in word_guessed with the guess from user input
                    self.word_guessed[i] = guess

            # Reduces num_letters by 1
            self.num_letters -= 1

        else:
            self.num_lives -= 1  
            print(f"Sorry, '{guess}' is not in the word!")
            print(f"You have {self.num_lives} lives left!!")

# Method to ask the user for input of a sinlge character that is alphabetical 

    def ask_for_input(self):
            while True:
                guess = input("Guess a letter: ")
                if len(guess) != 1 or not guess.isalpha():
                    print("Invalid letter. Please, enter an alphabetical character")
                elif guess in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    self.check_guess(guess)  

                    # Appends the guess to list_of_guesses
                    self.list_of_guesses.append(guess)  
                    break  

# This will call my class and methods to start plating the game - only allows one guess then I gues 'command not found'
 
hangman_game = Hangman(word_list)

hangman_game.ask_for_input()