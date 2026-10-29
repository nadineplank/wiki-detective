import sys

import cases

from game_logic import reveal_next_clue, check_guess, calculate_score
from investigation import run_investigation, retrieve_article


def display_main_menu():
    """Display the main menu."""
    print("🔎 WIKIPEDIA DETECTIVE")
    print()
    print("Every article holds a clue. Can you solve the mystery?")
    print()
    print("MAIN MENU")
    print("---")
    print("1. Start a new investigation")
    print("2. Quit the game")
    print("---")

def display_case_success(case, score, article_url):
    """Display the case success."""
    print()
    print("🔎 THE FINAL PIECE OF THE PUZZLE!")
    print("---")
    print("The evidence was there all along...")
    print()
    print(f"🎉 CASE SOLVED! The mystery person was {case.answer}!")
    print("Excellent detective work! You've cracked the case.")
    print()
    print(f"🏆 Your score: {score} points")
    print()
    print("📚 VERIFIED SOURCE")
    print(f"Wikipedia: {article_url}")
    print("---")

def select_case():
    """
    Display available mystery cases and prompt the player to select one.

    Returns:
        Case: The selected mystery case.
        None: If the player chooses to return to the main menu.
    """
    print("---")
    print("CHOOSE YOUR MYSTERY")
    print()
    print("Select a case to investigate:")
    print("---")

    for i, case in enumerate(cases.cases):
        print(f"{i + 1}. {case.title} - {case.difficulty.value}")

    print("---")
    print("0. ↩ Return to main menu")
    print()

    while True:
        try:
            user_input = int(input("Enter your choice (0-3): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_input not in range(0, len(cases.cases) + 1):
            print("Please enter a valid number.")
            continue

        if user_input == 0:
            return None

        return cases.cases[user_input - 1]


def play_game(case):
    used_clues = 0
    print("🕵️ INVESTIGATION STARTED")
    print(f"Case: {case.title}")
    print("---")
    print()
    print("CASE BRIEFING")
    print(case.description)
    print()
    print("Your mission: uncover the identity of the mystery person.")
    print("Search Wikipedia articles for clues, connect the evidence,")
    print("and make your guess when you're ready.")
    print()
    print("---")

    while True:
        print("What would you like to do? ")
        print("---")
        print("1. Investigate another Wikipedia article")
        print("2. Reveal a clue")
        print("3. Make a guess")
        print("---")
        print("0. ↩ Return to main menu")
        print()

        try:
            user_input = int(input("Enter your choice (0-3): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_input not in range(0, 4):
            print("Please enter a valid number.")
            continue

        if user_input == 0:
            break

        if user_input == 1:
            run_investigation()

        elif user_input == 2:
            used_clues = reveal_next_clue(case, used_clues)

        else:
            guess = input("What's your guess: ")
            result = check_guess(guess, case)
            if result:
                score = calculate_score(case, used_clues)
                article = retrieve_article(case.answer)
                display_case_success(case, score, article["url"])
                break
            else:
                print()
                print("🕵️ CASE STILL OPEN!")
                print("That's not the person we're looking for.")
                print("There's more evidence to uncover, detective!")
                print()


if __name__ == '__main__':
    test_case = cases.case_001
    print(test_case.title)
    print(test_case.description)
    print(test_case.clues)
    play_game(test_case)

