import requests as req
from bs4 import BeautifulSoup


class NativeParser:
    def __init__(self):
        self.url = "https://a1excode.netxisp.host/"
        self.soup = BeautifulSoup(self.__get_page_query(), 'html.parser')

    def __get_page_query(self):
        return req.get(self.url).text

    def __get_all_from_html_to_txt(self, name, class_name):
        return self.soup.find_all(name, class_=class_name)

    def __parse_top_post(self):
        return self.soup.find('div', {'class', 'col-12'})

    def parse_six_last_native(self):
        return self.__get_all_from_html_to_txt('div', 'col-md-6')

    def get_list_six_last_news(self):
        news_list = []

        n = 3
        while n < 21:
            if n % 3:
                news_list.append({
                    "title": BeautifulSoup(
                        str(self.parse_six_last_native()[n]),
                        'html.parser').find('h3', class_="font-weight-bold"),

                    "mini_text": BeautifulSoup(
                        str(self.parse_six_last_native()[n]),
                        'html.parser').find('p', class_="text-muted"),

                    "post_url": BeautifulSoup(
                        str(self.parse_six_last_native()[n]),
                        'html.parser').find('a', class_="btn btn-success")
                })
                n = n + 1
            n = n + 1

        return news_list
