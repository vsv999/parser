# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
import json
from ..items import AllocineTestItem, AllocineTestItemLoader


class AllocineSpider(CrawlSpider):
    name = 'allocine'
    allowed_domains = ['allocine.fr']
    start_urls = [
        'http://www.allocine.fr/films/',
        'http://www.allocine.fr/series-tv/'
    ]
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//ul[@data-name='Par genres']/li/a")),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='pagination-item-holder']/a")),
        Rule(LinkExtractor(restrict_xpaths="//h2[@class='meta-title']/a"), callback='parse_item'),
    )

    def parse_item(self, response):
        selector = Selector(response)
        l = AllocineTestItemLoader(AllocineTestItem(), selector)
        js = json.loads(response.xpath("//script[@type='application/ld+json']/text()").get().replace("\r", "").replace("\n", ""))
        l.add_value('type', js.get("@type"))
        if js.get("@type") == 'TVSeries':
            l.add_value('poster', js.get("image").split('?')[0])
        else:
            l.add_value('poster', js.get("image").get("url").split('?')[0])
        l.add_value('title', js.get("name"))
        l.add_value('number_seasons', js.get("numberOfSeasons"))
        l.add_value('number_episodes', js.get("numberOfEpisodes"))
        l.add_value('genre', js.get("genre"))
        l.add_value('description', js.get("description"))

        for i in response.xpath('//div[contains(@class, "card person-card")]'):
            l.add_value("stars", {"name": i.xpath('.//a[@class="meta-title-link"]/text()').get(),
                                  "image": i.xpath('.//img/@data-src').get()})
        for i in response.xpath('//span[contains(@class, "nationality")]/text()').getall():
            l.add_value("country", i.strip().title())
        for i in response.xpath('//div[@class="shot-holder cf"]//img'):
            l.add_value("images", {"url": i.xpath(".//@data-src").get(),
                                   "alt": i.xpath(".//@alt").get()})

        yield l.load_item()
