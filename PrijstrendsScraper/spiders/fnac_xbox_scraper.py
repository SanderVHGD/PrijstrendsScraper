import scrapy


class ProductsSpider(scrapy.Spider):
    name = "fnac_xbox"
    start_urls = [
        'https://www.nl.fnac.be/Microsoft-Xbox-Series-X-Console-Zwart/a15089504'
    ]

    def parse(self, response):
        for offer in response.css("li.js-fnacOffersTab"):
            yield {
                'price': offer.css("span.f-productOffers-tabLabel--price::text").get().replace('\xa0',''),
            }

#https://medium.com/codelog/store-scrapy-crawled-data-in-postgressql-2da9e62ae272