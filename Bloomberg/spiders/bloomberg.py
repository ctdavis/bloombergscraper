from scrapy import Spider, Request
from scrapy.loader import ItemLoader
from Bloomberg.items import Article
import re
import hashlib

class BloombergSpider(Spider):
    name = 'bloomberg'
    start_urls = ['https://www.bloomberg.com/search?query={}&page={}']

    def __init__(self, section='stocks', n_pages=5, *args, **kwargs):
        super(BloombergSpider, self).__init__(self, *args, **kwargs)
        self.n_pages = int(n_pages)
        self.section = section
        self.article_list = '//h1[@class="search-result-story__headline"]'+\
                            '/a[not(contains(@href,"/videos"))'+\
                            'and not(contains(@href,"/audio"))]'+\
                            '/@href'
        self.title = '//*[self::span[contains(@class,"lede-") and contains(@class,"__highlight")]'+\
                     'or self::h1[contains(@class,"headline_")]/a]'+\
                     '/text()'
        self.text = '//div[@class="body-copy"]/p/text()'
        self.date_written = '//time[@class="article-timestamp"]/@datetime'

    def start_requests(self):
        yield Request(self.start_urls[0].format(self.section, 1), callback=self.parse)

    def parse(self, response):
        for article in response.xpath(self.article_list).extract():
            yield Request(article, callback=self.parse_article)

        current_page = int(re.sub(r'^.*&page=(\d+).*$',r'\1',response.url)) + 1

        if current_page <= self.n_pages:
            yield Request(self.start_urls[0].format(self.section, current_page), callback=self.parse)


    def parse_article(self, response):

        item = ItemLoader(Article())

        item.add_value('title', response.xpath(self.title).extract_first())
        item.add_value('text', response.xpath(self.text).extract())
        item.add_value('date_written', response.xpath(self.date_written).extract_first())
        item.add_value('url', response.url)
        item.add_value('section', self.section)
        item.add_value('_id', self.hash_id(response.xpath(self.title).extract_first() + response.url))

        return item.load_item()

    def hash_id(self, url):
        hid = hashlib.sha1(url.encode('utf-8'))
        return hid.hexdigest()
