import scrapy


class ProductsSpider(scrapy.Spider):
    name = "fnac"
    start_urls = [
        'https://www.nl.fnac.be/Alle-TV-s/TV-Televisie-s/nsh474940?sl'
    ]

    def parse(self, response):
        #for item in response.xpath('//div[contains(@class, "Article-item")]'):
        for item in response.css('div.Article-item'):
            yield {
                'name': item.xpath('normalize-space(.//a[contains(@class, "Article-title")]/text())').get(),
                #'name': item.css('a.Article-title::text').get(),
                'availability': item.xpath('normalize-space(.//span[contains(@class, "Dispo-txt")]/text())').get(),
                #'availability': item.css('span.Dispo-txt::text').get(),
                'price': item.xpath('normalize-space(.//strong[contains(@class, "userPrice")]/text())').get().replace('\xa0',''),
                #'price': item.css('strong.userPrice::text').get(),
                'discounted_price': item.xpath('normalize-space(.//a[contains(@class, "userPrice")]/text())').get().replace('\xa0','')
                #'discounted_price': item.css('a.userPrice::text').get()
            }

#https://medium.com/codelog/store-scrapy-crawled-data-in-postgressql-2da9e62ae272