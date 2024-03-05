# import requests
#
# URL = 'https://www.championat.com/news/1.html?utm_source=button&utm_medium=news'
#
# HEADERS = {
#     "Accept-Language":
#         "en-GB,en;q=0.5",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
# }
#
# response = requests.request(method="GET", url=URL, headers=HEADERS)
# print(response.text)
import requests
from parsel import Selector


class EnglishScrapper:
    URL = "https://test-english.com/level-b2/"
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
        'Accept': 'application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'identity'
    }
    LINKXPATH = '//div[@class="pill hoverable"]/a/@href'

    def parse_data(self):
        text = requests.get(url=self.URL, headers=self.HEADERS).text
        tree = Selector(text=text)
        links = tree.xpath(self.LINKXPATH).extract()
        for link in links:
            print(link)
        return links


if __name__ == '__main__':
    scrapper = EnglishScrapper()
    scrapper.parse_data()
