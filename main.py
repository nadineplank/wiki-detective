import cases

from game_logic import reveal_next_clue, check_guess, calculate_score
from investigation import run_investigation, retrieve_article
from ai.mystery_generator import generate_mystery
from case import Difficulty

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

    Players can choose a predefined case, generate a mystery by topic,
    or return to the main menu.

    Returns:
        Case: The selected predefined or AI-generated mystery case.
        None: If the player chooses to return to the main menu.
    """
    print("---")
    print("CHOOSE YOUR MYSTERY")
    print()
    print("Select a case to investigate:")
    print("---")

    for i, case in enumerate(cases.cases):
        print(f"{i + 1}. {case.title} - {case.difficulty.value}")

    ai_option = len(cases.cases) + 1

    print(f"{ai_option}. Generate a mystery by topic")

    print("---")
    print("0. ↩ Return to main menu")
    print()

    while True:
        try:
            user_input = int(input(f"Enter your choice (0-{ai_option}): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_input not in range(0, ai_option + 1):
            print("Please enter a valid number.")
            continue

        if user_input == 0:
            return None

        if user_input == ai_option:
            topic = input("What topic would you like to investigate? ").strip()

            if not topic:
                print("Please enter a topic.")
                continue

            for i, difficulty in enumerate(Difficulty):
                print(f"{i + 1}. {difficulty.value}")

            while True:
                try:
                    difficulty_input = int(input("What difficulty would you like (1-3)? " ))

                except ValueError:
                    print("Please enter a valid number.")
                    continue

                difficulty = list(Difficulty)[difficulty_input -1]
                generated_case = generate_mystery(topic, difficulty)
                return generated_case

        return cases.cases[user_input - 1]


def play_game(case):
    """
    Run the investigation game for the selected case.

    Args:
       case: The mystery case selected by the player.

   """
    used_clues = 0
    print()
    print("🕵️ INVESTIGATION STARTED")
    print(f"Case: {case.title}")
    print("---")
    print()
    print("🗂️CASE BRIEFING")
    print(case.description)
    print()
    print("Your mission: uncover the identity of the mystery person.")
    print("Search Wikipedia articles for clues, connect the evidence,")
    print("and make your guess when you're ready.")
    print("---")

    while True:
        print()
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


def main():
    """
    Run the main game loop.

    Display the main menu, handle the player's choice, and coordinate
    case selection and gameplay until the player chooses to quit.
    """

    while True:
        display_main_menu()

        try:
            user_input = int(input("Enter your choice (1-2): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_input not in range(1, 3):
            print("Please enter a valid number.")
            continue

        if user_input == 1:
            selected_case = select_case()

            if selected_case:
                play_game(selected_case)

        if user_input == 2:
            print("---")
            print("Thanks for playing Wikipedia Detective! 🕵️")
            break


if __name__ == '__main__':
    main()

