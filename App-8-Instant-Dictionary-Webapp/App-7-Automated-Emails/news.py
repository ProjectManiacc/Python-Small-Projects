import requests
import urllib3

urllib3.disable_warnings()


#
class NewsFeed:
    base_url = 'https://newsapi.org/v2/everything?'
    apiKey = 'abfaf02985c64e948e5f22a2375349ca'

    def __init__(self, interest, from_date, to_date, language='en'):
        self.language = language
        self.to_date = to_date
        self.from_date = from_date
        self.interest = interest

    def get(self):
        url = self._build_url()
        articles = self._get_articles(url)

        email_body = ''
        for article in articles:
            email_body += article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

    def _get_articles(self, url):
        response = requests.get(url, verify=False)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f'{self.base_url}' \
              f'q={self.interest}&' \
              f'from={self.from_date}&' \
              f'to={self.to_date}&' \
              f'language={self.language}&' \
              f'apiKey={self.apiKey}'
        return url

