"""
@date: 10/04/2024
@name: pwordle.py
@author: github.com/chrvstian
"""

from string import ascii_letters
from rich.console import Console
from rich.theme import Theme
from random import choice
from typing import List

import pathlib

# Create a Console object with customized width and theme
console: Console = Console(
    width=40,
    theme=Theme({"warning": "red on yellow"})
)

def generate_word() -> str:
    """Pick a random word from a file.

    Returns:
        str: A randomly chosen word.
    """
    with open("words.txt", 'r') as file:
        return choice(choice(file.readlines()).split()).strip()

def main() -> None:
    """Main function to execute the game."""
    # Generate a word and convert it to uppercase
    word: str = generate_word().upper()
    # Initialize guesses as a list of underscores
    guesses: List[str] = ["_" * 5] * 6

    # Iterate over the number of allowed guesses
    for idx in range(6):
        refresh_page(headline=f"Guess {idx + 1}")
        show_guesses(guesses, word)

        guesses[idx] = guess_word(previous_guesses=guesses[:idx])
        # Break the loop if the guessed word matches the target word
        if guesses[idx] == word:
            break

    game_over(guesses, word, guessed_correctly=guesses[idx] == word)

def refresh_page(headline: str) -> None:
    """Clear the console and display a new headline.

    Args:
        headline (str): The headline to display.
    """
    console.clear()
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")

def show_guesses(guesses: List[str], word: str) -> None:
    """Display the current guesses.

    Args:
        guesses (List[str]): List of guesses.
        word (str): The target word.
    """
    for guess in guesses:
        styled_guess: List[str] = []
        for letter, correct in zip(guess, word):
            if letter == correct:
                style: str = "bold white on green"
            elif letter in word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]")

        console.print("".join(styled_guess), justify="center")

def guess_word(previous_guesses: List[str]) -> str:
    """Prompt the user for a guess and validate it.

    Args:
        previous_guesses (List[str]): List of previous guesses.

    Returns:
        str: The validated guess.
    """
    guess: str = console.input("\nGuess word: ").upper()

    if guess in previous_guesses:
        console.print(f"You've already guessed {guess}.", style="warning")
        return guess_word(previous_guesses)

    if len(guess) != 5:
        console.print("Your guess must be 5 letters.", style="warning")
        return guess_word(previous_guesses)

    if any((invalid := letter) not in ascii_letters for letter in guess):
        console.print(
            f"Invalid letter: '{invalid}'. Please use English letters.",
            style="warning",
        )
        return guess_word(previous_guesses)

    return guess

def game_over(
        guesses: List[str],
        word: str,
        guessed_correctly: bool
    ) -> None:
    """Display the game result.

    Args:
        guesses (List[str]): List of guesses.
        word (str): The target word.
        guessed_correctly (bool): Indicates if the word was guessed correctly.
    """
    refresh_page(headline="Game Over")
    show_guesses(guesses, word)

    if guessed_correctly:
        console.print(f"\n[bold white on green]Correct, the word is {word}![/]")
    else:
        console.print(f"\n[bold white on red]Sorry, the word was {word} :( [/]")

if __name__ == "__main__":
    main()
