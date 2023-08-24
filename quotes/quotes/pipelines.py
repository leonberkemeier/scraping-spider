# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class QuotesPipeline:
    def process_item(self, item, spider):
        return item

class SqliteDemoPipeline:

    def __init__(self):
        #create/connect to db
        self.con = sqlite3.connect('demo.db')
        #create cursor 
        self.cur = self.con.cursor()

        #create table if none exist
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS quotes(
            text TEXT,
            tags TEXT,
            author TEXT
        )
        """)        

    def process_item(self, item, spider):
        
        ## Define insert statement
        self.cur.execute("""
            INSERT INTO quotes (text, tags, author) VALUES (?, ?, ?)
        """,
        (
            item['text'],
            str(item['tags']),
            item['author']
        ))

        ## Execute insert of data into database
        self.con.commit()
        return item
