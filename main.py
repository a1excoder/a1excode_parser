import requests as req
from bs4 import BeautifulSoup as bs


class Main:
    def __init__(self):
        self.url = "https://a1excode.netxisp.host/"

    def get_page_query(self):
        return req.get(self.url).text

    def parse_six_last_news(self):
        pass


if __name__ == '__main__':
    main = Main()
    print(main.get_page_query())
