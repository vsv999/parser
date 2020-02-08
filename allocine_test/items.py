# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, Identity, MapCompose, Compose
from scrapy.loader import ItemLoader


class AllocineTestItem(scrapy.Item):
    type = scrapy.Field(output_processor=TakeFirst())
    title = scrapy.Field(output_processor=TakeFirst())
    poster = scrapy.Field(output_processor=TakeFirst())
    number_seasons = scrapy.Field(output_processor=TakeFirst())
    number_episodes = scrapy.Field(output_processor=TakeFirst())
    genre = scrapy.Field()
    description = scrapy.Field(output_processor=TakeFirst())
    stars = scrapy.Field()
    country = scrapy.Field()
    images = scrapy.Field()


class AllocineTestItemLoader(ItemLoader):
    type = TakeFirst()
    title = TakeFirst()
    poster = TakeFirst()
    number_seasons = TakeFirst()
    number_episodes = TakeFirst()
    genre = TakeFirst()
    description = TakeFirst()
    stars = TakeFirst()
    country = TakeFirst()
    images = TakeFirst()



