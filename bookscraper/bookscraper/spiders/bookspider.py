import scrapy
import pandas as pd
from bookscraper.items import BookItem
import datetime
import os

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]


    custom_settings={
        'FEED': {
            'booksdata.json': {'format': 'json', 'overwrite': True},
        }
    }



    def parse(self, response):
        books = response.css('article.product_pod')
        

        # for book in books:
        #     yield{
        #         'name' : book.css('h3 a::text').get(),
        #         'price' : book.css('.product_price .price_color::text').get(),
        #         'url' : books.css('h3 a'.attrib['href'])
        #     }
        
        # next_page = response.css('li.next a ::attr(href)').get()

        # if next_page is not None:
        #     if 'catalogue/' in next_page:
        #         next_page_url = 'https://books.toscrape.com/' + next_page
        #     else:
        #         next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
        #     yield response.follow(next_page_url, callback= self.parse)


        # next step to collect the data and safe to json file :
    def parse(self, response):
        
        books = response.css('article.product_pod')
        
        for book in books:
            relative_url = book.css('h3 a ::attr(href)').get()

            if 'catalogue/' in relative_url:
                book_url = 'https://books.toscrape.com/' + relative_url
            else:
                book_url = 'https://books.toscrape.com/catalogue/' + relative_url
            yield response.follow(book_url, callback= self.parse_book_page)

            next_page = response.css('li.next a ::attr(href)').get()

            # if next_page is not None:
            #     if 'catalogue/' in next_page:
            #         next_page_url = 'https://books.toscrape.com/' + next_page
            #     else:
            #         next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
            #     yield response.follow(next_page_url, callback= self.parse)


    
    def parse_book_page(self, response):

        table_rows = response.css("table tr")

        

        # yield {
        #     'url' : response.url,
        #     'title' : response.css(".product_main h1::text").get(),
        #     'price_excl_tax' :table_rows[2].css("td ::text").get(),
        #     'stars' : response.css("p.star-rating").attrib['class'],
        #     'category' : response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
        #     'description' : response.xpath("//div[@id='product_description']/following-sibling::p/text()").get(),
        #     'price' : response.css('p.price_color ::text').get(),
        # }


###########
        # yield {
        #     'url' : response.url,
        #     'title' : response.css(".product_main h1::text").get(),
        #     # 'price_excl_tax' :table_rows[2].css("td ::text").get(),
        #     # 'stars' : response.css("p.star-rating").attrib['class'],
        #     # 'category' : response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
        #     # 'description' : response.xpath("//div[@id='product_description']/following-sibling::p/text()").get(),
        #     'price' : response.css('p.price_color ::text').get(),
        # }
##############        
        





                    # name = []
                    # price = []
                    # url = []

                    # my_dict = {'name' : name, 'price': price, 'link' : url}

                    # bookinfo = pd.DataFrame(my_dict)

                    # bookinfo.to_csv('bookinfo')
       
       
        # yield{
        #     'name' : response.css('.product_main h1::text').get(),
        #     'url' : response.url,  
        #     'price' : table_rows[2].css("td ::text").get(),
        # }

        book_item = BookItem()

        book_item['name'] = response.css('.product_main h1::text').get(),
        book_item['url'] = response.url,
        # book_item['price'] = table_rows[2].css("td ::text").get()
        book_item['price'] = response.css('p.price_color ::text').get(),
        
#without pipeline

        # yield BookItem

#with pipeline
        yield book_item