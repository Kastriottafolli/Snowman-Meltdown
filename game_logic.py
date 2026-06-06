"""
game_logic.py – Core game logic for Snowman Meltdown.
Contains word selection, display, and the main game loop.
"""

import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

MAX_MISTAKES = len(STAGES) - 1  # 4 mistakes allowed


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Displays the current snowman stage and the word with blanks
    for unguessed letters.
    """
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print()


def is_word_guessed(secret_word, guessed_letters):
    """Returns True if all letters of the secret word have been guessed."""
    return all(letter in guessed_letters for letter in secret_word)


def get_valid_guess(guessed_letters):
    """
    Prompts the user for a single alphabetical letter.
    Re-prompts on invalid input or already-guessed letters.
    """
    while True:
        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1:
            print("Please enter exactly one letter.")
        elif not guess.isalpha():
            print("Please enter an alphabetical character.")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        else:
            return guess


def play_game():
    """Main game loop for Snowman Meltdown."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check win condition
        if is_word_guessed(secret_word, guessed_letters):
            print("Congratulations! You saved the snowman! The word was:", secret_word)
            break

        # Check lose condition
        if mistakes >= MAX_MISTAKES:
            print(STAGES[MAX_MISTAKES])
            print("Oh no! The snowman has melted! The word was:", secret_word)
            break

        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            mistakes += 1
            remaining = MAX_MISTAKES - mistakes
            print(f"Wrong! '{guess}' is not in the word. {remaining} mistake(s) remaining.")


def main():
    """Entry point: run the game and offer a replay option."""
    while True:
        play_game()
        again = input("\nWould you like to play again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing Snowman Meltdown! Goodbye!")
            break
        print("\n" + "=" * 40 + "\n")
