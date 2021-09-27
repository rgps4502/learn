import scrapy


class CheapssSeliumeSpider(scrapy.Spider):
    name = 'cheapss_seliume'
    allowed_domains = ['cheapsslsecurity.com/quicklogin.html?isauth=false']
    start_urls = ['http://cheapsslsecurity.com']

    def parse(self, response):
        pass
