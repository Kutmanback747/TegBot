# from parsel import Selector
# import httpx
# import asyncio
#
# class AsyncScraper:
#     PLUS_URL = 'https://www.championat.com'
#     URL = 'https://www.championat.com/news/1.html?utm_source=button&utm_medium=news'
#     HEADERS = {
#         "Accept-Language":
#             "en-GB,en;q=0.5",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
#     }
#
#     LINK_XPATH = '//div[@class="news-item__content"]/a/@href'
#
#     async def fetch_page(self, client, page):
#         try:
#             url = self.URL.format(page=page)
#             response = await client.get(url, timeout=10.0)
#             print(f"Страница: {page}")
#
#             if response.status_code == 200:
#                 return Selector(text=response.text)
#             else:
#                 response.raise_status()
#         except httpx.ReadTimeout:
#             print(f"ReadTimeoutError on page: {page}")
#             return None
#
#     async def scrape_page(self, selector):
#         links = selector.xpath(self.LINK_XPATH).getall()
#         print(links)
#
#     async def get_pages(self, limit=5):
#         async with httpx.AsyncClient(headers=self.HEADERS) as client:
#             tasks = [self.fetch_page(client=client, page=page) for page in range(1, limit + 1)]
#             pages = await asyncio.gather(*tasks)
#             scrape_tasks = [self.scrape_page(page) for page in pages if page is not None]
#             await asyncio.gather(*scrape_tasks)
#
#
# if __name__ == "__main__":
#     scraper = AsyncScraper()
#     asyncio.run(scraper.get_pages())
from parsel import Selector
import httpx
import asyncio


class AsyncEnglishScrapper:
    URL = "https://test-english.com/level-b2/"
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
        'Accept': 'application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'identity'
    }
    ADVXPATH = '//div[@class="pill hoverable"]/a/@href'
    ALLXPATH = '//div[@class="dropdown-menu "]/a/@href'

    async def get_page(self):
        async with httpx.AsyncClient(headers=self.HEADERS) as client:
            response = await client.get(url=self.URL)
            links_c1 = await self.c1(response=response)
            links_b2 = await self.b2(response=response)
            links_b1 = await self.b1(response=response)
            links_a2 = await self.a2(response=response)
            links_a1 = await self.a1(response=response)
            l = [links_c1, links_b2, links_b1, links_a2, links_a1]
            return l

    async def c1(self, response):
        tree = Selector(text=response.text)
        links = tree.xpath(self.ADVXPATH).extract()
        for link in links:
            print(link)
        return links

    async def b2(self, response):
        tree = Selector(text=response.text)
        links = tree.xpath(self.ALLXPATH).extract()[3:29:5]
        for i in links:
            print(i)
        return links

    async def b1(self, response):
        tree = Selector(text=response.text)
        links = tree.xpath(self.ALLXPATH).extract()[2:29:5]
        for link in links:
            print(link)
        return links

    async def a2(self, response):
        tree = Selector(text=response.text)
        links = tree.xpath(self.ALLXPATH).extract()[1:29:5]
        for link in links:
            print(link)
        return links

    async def a1(self, response):
        tree = Selector(text=response.text)
        links = tree.xpath(self.ALLXPATH).extract()[0:29:5]
        for link in links:
            print(link)
        return links

    @classmethod
    def scrape_data(cls):
        pass


if __name__ == "__main__":
    scraper = AsyncEnglishScrapper()
    asyncio.run(scraper.get_page())
