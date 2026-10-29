import wikipediaapi

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
            print(f"Article: {article['title']}")
            print(f"URL: {article['url']}")
            print(f"Summary: {article['summary']}")
            print(" ")
            return
