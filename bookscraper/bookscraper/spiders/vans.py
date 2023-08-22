import scrapy


class VansSpider(scrapy.Spider):
    name = "vans"
    allowed_domains = ["vans.com"]
    start_urls = ["https://vans.com"]

    def parse(self, response):
        pass


#for shoe type
#response.css('.product-info h1::text').get()


#for price 
#