# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from book.items import BookItem

class ArticleSpider(scrapy.Spider):
    name = "article"
    allowed_domains = ["23txt.com"]
    start_urls = (
        'https://www.23txt.com/files/article/html/43/43988/15976998.html',
    )

    def parse(self, response):
    	title_xpath="//div[@class='bookname']/h1/text()"
    	body_xpath="//div[@id='content']/text()"
        next_page_xpath="//div[@class='bottem1']/a[3]/@href"
        body = response.body.decode('gbk')
        item = BookItem()
        item["title"] = Selector(text=body).xpath(title_xpath).extract()[0]
        item["body"] = '\n'.join(Selector(text=body).xpath(body_xpath).extract()[1:])
        yield item
        url = Selector(text=body).xpath(next_page_xpath).extract()[0]
        yield scrapy.Request("https://www.23txt.com"+url)
        

