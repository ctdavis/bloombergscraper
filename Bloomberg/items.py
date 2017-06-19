# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader.processors import Join, TakeFirst, Compose

def extra_space_stripper(text):
    return ' '.join(text).strip()

class Article(Item):

    url = Field(output_processor=TakeFirst())
    title = Field(
                input_processor=Compose(extra_space_stripper),
                output_processor=TakeFirst()
            )
    text = Field(
               input_processor=Compose(extra_space_stripper),
               output_processor=TakeFirst()
           )
    section = Field(output_processor=TakeFirst())
    date_written = Field(output_processor=TakeFirst())
    _id = Field(output_processor=TakeFirst())
