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


if __name__ == '__main__':
    article = retrieve_article('Ada Lovelace')
    if article is None:
        print('Article not found. Please check the title and try again.')
    else:
        print(f"Article: {article['title']}")
        print(f"URL: {article['url']}")
        print(f"Summary: {article['summary']}")

