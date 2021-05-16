import scrapy


class ProductsSpider(scrapy.Spider):
    name = "fnac"
    start_urls = [
        'https://www.nl.fnac.be/Alle-TV-s/TV-Televisie-s/nsh474940?sl'
    ]

    def parse(self, response):
        for item in response.xpath('//div[contains(@class, "Article-item")]'):
            print(item)
            yield {
                'name': item.xpath('//a[contains(@class, "Article-title")]/text()').get(),
                'availability': item.xpath('//li[contains(@class, "seller-item")]/p/@class').get,
                'price': item.css('//strong[contains(@class, "userPrice")]/text()').get(),
            }