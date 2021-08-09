import requests as req
from bs4 import BeautifulSoup


class Parser:
    def __init__(self):
        self.url = "https://a1excode.netxisp.host/"
        self.soup = BeautifulSoup(self.get_page_query(), 'html.parser')

    def get_page_query(self):
        return req.get(self.url).text

    def parse_six_last_news(self):
        pass

    def parse_top_post(self):
        return self.soup.find('a')

    def get_title_page(self):
        return self.soup.title.string


if __name__ == '__main__':
    parser = Parser()
    print(parser.get_title_page())
