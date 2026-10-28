import wikipediaapi
import cases


wiki_wiki = wikipediaapi.Wikipedia(user_agent='Wiki Detective (https://github.com/nadineplank/wiki-detective)', language='en')

def retrieve_article(title):
    """Retrieve a Wikipedia article by its title.

        Args:
            title: The title of the Wikipedia article to retrieve.

        Returns:
            A dictionary containing the article's URL, title, and summary,
            or None if the article does not exist.
        """
    page = wiki_wiki.page(title)
    if page.exists():
        return {
            "url": page.fullurl,
            "title": page.title,
            "summary": page.summary,
        }
    return None


def get_investigation_choice():
    """Prompt the player to choose their next investigation action.

    Returns:
        The player's validated choice: 'article' or 'guess'.
    """
    choices = ["article", "guess"]

    while True:
        choice = input(
            "Do you want to look at another article or make a guess? "
        ).strip().lower()

        if choice in choices:
            return choice

        print("Please make a valid choice: 'article' or 'guess'.")


def run_investigation():
    """Let the player investigate Wikipedia articles and make a guess."""
    while True:
        title = input("At which Wikipedia article do you want to look? ").strip()
        if title == "":
            print("Please enter Wikipedia article title ")
            continue

        article = retrieve_article(title)
        if article is None:
            print('Article not found. Please check the title and try again. ')
        else:
            print(f"Article: {article['title']}")
            print(f"URL: {article['url']}")
            print(f"Summary: {article['summary']}")
            print(" ")
            choice = get_investigation_choice()
            if choice == "article":
                continue
            elif choice == "guess":
                break

    guess = input("What's your guess?").strip()


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


def select_case():
    """Display available mystery cases and prompt the player to select one.

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


if __name__ == '__main__':
    test_case = cases.case_001
    print(test_case.title)
    print(test_case.description)
    print(test_case.clues)

