import scrapy
from scrapy.crawler import CrawlerProcess
import time
import os
import schedule
from bookscraper.items import ABookItem
from datetime import datetime
import logging

date = datetime.now()

# logger = logging.getLogger(__name__)

class AbookspiderSpider(scrapy.Spider):
    name = "abookspider"
    allowed_domains = ["books.toscrape.com"]
    # start_urls = ["https://books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"]


    def parse(self, response):

        
        books = response.css('article.product_pod')
        
        
        # yield{
        #     'name' : response.css('h1 ::text').get(),
        #     'price' : response.css('.price_color ::text').get(),
        #         }
        
# if __name__=="__main__":
#     process = CrawlerProcess({})


        abook_item = ABookItem()

        abook_item['name'] =response.css('h1 ::text').get(),
        abook_item['price'] =response.css('.price_color ::text').get(),
        
        # abook_item['time'] = date,
        # abook_item['time'] = time       

        yield abook_item
        # print(time)
    # def spider_closed(self, spider):
    #     logger.info("closed %s", spider.name)

    #
    #to save to sqlite database
    #https://scrapeops.io/python-scrapy-playbook/scrapy-save-data-sqlite/