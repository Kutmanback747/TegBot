from parsel import Selector
import httpx
import asyncio

class AsyncScraper:
    PLUS_URL = 'https://www.championat.com'
    URL = 'https://www.championat.com/news/1.html?utm_source=button&utm_medium=news'
    HEADERS = {
        "Accept-Language":"en-GB,en;q=0.5",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    }

    LINK_XPATH = '//div[@class="news-item__content"]/a/@href'

    async def get_page(self):
        async with httpx.AsyncClient(headers=self.HEADERS) as client:
            response = await client.get(url=self.URL)
            links_news=await self.news(response=response)
            links=[self.PLUS_URL+i for i in links_news][:5]
            return links



    async def news (self,response):
        tree = Selector(text=response.text)
        links = tree.xpath(self.LINK_XPATH).extract()
        return links


if __name__ == "__main__":
    scraper = AsyncScraper()
    asyncio.run(scraper.get_page())
