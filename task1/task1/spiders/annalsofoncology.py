import scrapy
from ..items import Task1Item


class AnnalsofoncologySpider(scrapy.Spider):
    name = 'annalsofoncology'
    allowed_domains = ['www.annalsofoncology.org']
    start_urls = ['https://www.annalsofoncology.org/issue/S0923-7534(21)X0008-7']

    def parse(self, response):
        for links in response.css('h3 > a::attr(href)'):
            yield response.follow(links.get(), callback=self.parse_items)

    def parse_items(self, response):
        items = Task1Item()

        title = response.css('div > h1').css(
            '::text').extract()
        pi = response.css(
            'div.article-header__wrapper > div > ul').css('::text').extract()
        links = response.css
        center = response.css('div.article-header__info__group > div').css(
            '::text').extract()

        items['title'] = title
        items['center'] = center
        items['pi'] = pi
        items['links'] = links

        yield items

