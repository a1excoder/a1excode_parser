from NativeParser import NativeParser


class Parser(NativeParser):

    def get_title_page(self):
        return self.soup.title.string

    def view_list_last_six_news(self):
        for post in NativeParser.get_list_six_last_news(self):
            print(f"title: {post['title'].text}\n\t"
                  f"query: {post['mini_text'].text}\n\t\t"
                  f"url: {post['post_url'].get('href')}\n")
