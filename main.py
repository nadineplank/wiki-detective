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


if __name__ == '__main__':
    test_case = cases.case_001
    print(test_case.title)
    print(test_case.description)
    print(test_case.clues)
    # run_investigation()

