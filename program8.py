"""
Write a Python program that retrieves the top stories from Google News.
"""
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup


def get_top_stories():
    url = 'https://news.google.com/topstories'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        top_stories = []

        for article in soup.find_all('article'):
            headline = article.find('h3', class_='ipQwMb ekueJc RD0gLb')
            source = article.find('a', class_='wEwyrc AVN2gc uQIVzc Sksgp')

            if headline and source:
                top_stories.append({
                    'headline': headline.text,
                    'source': source.text,
                    'link': 'https://news.google.com' + source['href']
                })

        return top_stories

    else:
        print("Failed to retrieve data from Google News.")
        return []


if __name__ == '__main__':
    top_stories = get_top_stories()

    if top_stories:
        print("Top Stories from Google News:")
        for idx, story in enumerate(top_stories, start=1):
            print(f"{idx}. {story['headline']} - {story['source']}")
            print(f"   Link: {story['link']}\n")
    else:
        print("No top stories found.")
