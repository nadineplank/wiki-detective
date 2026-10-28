import wikipediaapi


wiki_wiki = wikipediaapi.Wikipedia(user_agent='Wiki Detective (https://github.com/nadineplank/wiki-detective)', language='en')

def retrieve_article(title):
    """Retrieves article from Wikipedia"""
    page = wiki_wiki.page(title)
    if page.exists():
        return {
            "url": page.fullurl,
            "title": page.title,
            "summary": page.summary,
        }
    return None

def get_investigation_choice():
    choices = ["article", "guess"]

    while True:
        choice = input(
            "Do you want to look at another article or make a guess? "
        ).strip().lower()

        if choice in choices:
            return choice

        print("Please make a valid choice: 'article' or 'guess'.")


def run_investigation():
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

    run_investigation()

