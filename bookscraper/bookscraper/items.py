# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# from datetime import datetime

# timer = datetime.now()



class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def serialize_price(value):
    return f'$ {str(value)}'

class BookItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()


# class ABookItem(scrapy.Item):
#     name = scrapy.Field()
#     price = scrapy.Field()
#     time = scrapy.Field()
#     # time = timer


from scrapy.item import Item, Field

class ABookItem(Item):
    name = Field()
    price = Field()
    # time = Field()    