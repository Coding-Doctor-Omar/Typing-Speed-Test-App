import requests
from bs4 import BeautifulSoup

URL = "https://fungenerators.com/random/text/sentence"

class SentenceGenerator:
    def __init__(self):
        self.sentence = None

    def random_sentence(self):
        try:
            web_html = requests.get(url=URL, timeout=7).text
            soup = BeautifulSoup(web_html, "html.parser")
            self.sentence = soup.select_one(selector=".text-2xl").text.strip()
        except (requests.ConnectionError, requests.ConnectTimeout):
            return False
        else:
            return self.sentence


















