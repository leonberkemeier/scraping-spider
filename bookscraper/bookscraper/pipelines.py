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
    


