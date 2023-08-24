# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):


        adapter = ItemAdapter(item)

        ## Strip all whitespaces from strings
        field_names=adapter.field_names()

        # for field_name in field_names:
        #     # if field_name != 'description':
        #         value = adapter.get(field_name)
        #         adapter[field_name] = value[0].strip()

        ## Swichting to lowercase

        # lowercase_keys = ['category', 'product_type' ,'name']
        # for lowercas_key in lowercase_keys:
        #     value = adapter.get(lowercas_key)
        #     adapter[lowercas_key] = value.lower()


        # ## Convert price to floaat

        price_keys=['price']

        for price_key in price_keys:
            value=adapter.get(price_key)
            value=value[0].replace('£', '')
            # value=value.replace('$', '')
            # value=value.replace('€', '')
            adapter[price_key] = float(value)


        ## String to integer

        # num_reviews_string = adapter.get('num_reviews')
        # adapter['num_reviews'] = int(num_reviews_string)


        return item

import sqlite3
from itemadapter import ItemAdapter

# class Sql1tePipeline:
    
#     # def __init__(self):
#     #     #create/connect to db
#     #     self.con = sqlite3.connect('price.db')
#     #     #create cursor 
#     #     self.cur = self.con.cursor()

#     #     #create table if none exist
#     #     self.cur.execute("""
#     #     CREATE TABLE IF NOT EXISTS abook(
#     #         name TEXT,
#     #         price TEXT,
#     #         time TEXT
#     #     )
#     #     """)        

#     def process_item(self, item, spider):
        
#         adapter = ItemAdapter(item)

#         field_names=adapter.field_names()

#         price_keys=['price']

#         for price_key in price_keys:
#             value=adapter.get(price_key)
#             value=value[0].replace('£', '')
#             # value=value.replace('$', '')
#             # value=value.replace('€', '')
#             adapter[price_key] = float(value)
            
#         return item

#         ## Define insert statement
#         self.cur.execute("""
#             INSERT INTO abook (name, price, time) VALUES (?, ?, ?)
#         """,
#         (
#             item['name'],
#             item['price'],
#             item['time'],
#         ))

#         ## Execute insert of data into database
#         self.con.commit()
#         return item
    
class SqlitePipeline:

    def __init__(self):
        #create/connect to db
        self.con = sqlite3.connect('proice.db')
        #create cursor 
        self.cur = self.con.cursor()

        #create table if none exist
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS abook(
            name TEXT,
            price TEXT,
            time TEXT
        )
        """)        


    ############

    # def process_item(self, item, spider):


    #     adapter = ItemAdapter(item)

    #     ## Strip all whitespaces from strings
    #     field_names=adapter.field_names()

    #     # for field_name in field_names:
    #     #     # if field_name != 'description':
    #     #         value = adapter.get(field_name)
    #     #         adapter[field_name] = value[0].strip()

    #     ## Swichting to lowercase

    #     # lowercase_keys = ['category', 'product_type' ,'name']
    #     # for lowercas_key in lowercase_keys:
    #     #     value = adapter.get(lowercas_key)
    #     #     adapter[lowercas_key] = value.lower()


    #     # ## Convert price to floaat

    #     price_keys=['price']

    #     for price_key in price_keys:
    #         value=adapter.get(price_key)
    #         value=value[0].replace('£', '')
    #         # value=value.replace('$', '')
    #         # value=value.replace('€', '')
    #         adapter[price_key] = float(value)


    #     ## String to integer

    #     # num_reviews_string = adapter.get('num_reviews')
    #     # adapter['num_reviews'] = int(num_reviews_string)


    #     return item
    
    #################
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        ## Strip all whitespaces from strings
        field_names=adapter.field_names()
        # ## Convert price to floaat
        price_keys=['price']
        for price_key in price_keys:
            value=adapter.get(price_key)
            value=value[0].replace('£', '')
            value=value.replace('$', '')
            value=value.replace('€', '')
            adapter[price_key] = float(value)
        #     return item
           
        self.cur.execute("""
            INSERT INTO abook (name, price, time) VALUES (?, ?, ?)
        """,
        (
            str(item['name']),        
            item['price'],
            str(item['time']),
        ))

        self.con.commit()
        return item


