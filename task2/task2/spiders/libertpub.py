import scrapy
from ..items import Task2Item

class LibertpubSpider(scrapy.Spider):
    name = 'libertpub'
    allowed_domains = ['www.liebertpub.com']
    start_urls = ['https://www.liebertpub.com/doi/full/10.1089/neu.2021.29111.abstracts']

    def parse(self, response):
        items = Task2Item()

        title = response.css('div > h4').css(
            '::text').extract()
        center = response.css('div > p > i').css(
            '::text').extract()
        pi = response.xpath(
            './/div[@class="article__body "]//p[.//u[@class] | .//i[.//sup]][.//sup]').xpath(
            'text()').getall()

        items['title'] = title
        items['center'] = center
        items['pi'] = pi

        yield items