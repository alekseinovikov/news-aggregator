import requests
from bs4 import BeautifulSoup


class HabrAggregator:
    url = "http://habr.com/ru/"

    def extract_title_and_link(self, post):
        title_tag = post.find(class_="post__title")
        title = title_tag.a.string
        link = title_tag.a['href']

        stats = post.find(class_="post-stats__result-counter")
        stats_counter = stats.string.replace('+', '')

        return title, link, float(stats_counter)

    def aggregate(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, 'html.parser')
        post_previews = soup.find_all(class_="post_preview")

        results = []
        for post in post_previews:
            result = self.extract_title_and_link(post)
            results.append(result)

        return results
