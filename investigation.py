import wikipediaapi
from rich.console import Console


wiki_wiki = wikipediaapi.Wikipedia(user_agent='Wiki Detective (https://github.com/nadineplank/wiki-detective)', language='en')
console = Console()


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
            "sections": page.sections,
        }
    return None


def run_investigation():
    """Let the player investigate Wikipedia articles."""

    while True:
        title = input("At which Wikipedia article do you want to look? ").strip()
        if title == "":
            print("Please enter Wikipedia article title ")
            continue

        article = retrieve_article(title)
        if article is None:
            print('Article not found. Please check the title and try again. ')
        else:
            print()
            print(f"Article: {article['title']}")
            print(f"URL: {article['url']}")
            console.print(f"Summary: {article['summary']}")
            print(" ")

            return article


def explore_sections(article):
    """
    Let the player explore Wikipedia sections.

    Args:
        article: The last Wikipedia article that the user explored.
    """

    if not article["sections"]:
        print("This article has no sections to explore. ")
        return

    title = article["title"]

    print()
    print(f"Which section of the article {title} do you want to explore? ")
    print("---")

    for i, section in enumerate(article["sections"]):
        print(f"{i + 1}. {section.title}")

    print("---")

    while True:
        try:
            user_input = int(input("Which section do you want to explore? "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if user_input not in range(1, len(article["sections"]) + 1):
            print(f"Please enter a valid number between 1 and {len(article['sections'])}")
            continue

        section = article["sections"][user_input - 1]

        print()
        print(section.title)
        console.print(section.text)
        print()
        return

