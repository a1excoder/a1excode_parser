import requests as req
from bs4 import BeautifulSoup


class Parser(object):
    def __init__(self):
        self.url = "https://a1excode.netxisp.host/"
        self.soup = BeautifulSoup(self.__get_page_query(), 'html.parser')

    def __get_page_query(self):
        return req.get(self.url).text

    def __parse_six_last_native(self):
        return self.soup.find_all('div', class_="col-md-6")

    def view_six_last_news_native(self):
        n = 3
        while n < 21:
            if n % 3:
                print(self.__parse_six_last_native()[n], "\n\n")
                n = n + 1
            n = n + 1

    def get_list_six_last_news(self):
        news_list = []
        true_list = []

        n = 3
        while n < 21:
            if n % 3:
                news_list.append(self.__parse_six_last_native()[n])
                n = n + 1
            n = n + 1

        for post in news_list:
            true_list.append({
                "title": BeautifulSoup(post, 'html.parser').find('h3', class_="font-weight-bold"),
                "mini_text": BeautifulSoup(post, 'html.parser').find('p', class_="text-muted"),
                "post_url": BeautifulSoup(post, 'html.parser').find('a', class_="btn btn-success")
            })

        return true_list

    def parse_top_post(self):
        return self.soup.find('div', {'class', 'six-last'})

    def get_title_page(self):
        return self.soup.title.string


if __name__ == '__main__':
    parser = Parser()

    for i in parser.get_list_six_last_news():
        print(i)
