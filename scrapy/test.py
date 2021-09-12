
import scrapy


class animeSpider(scrapy.Spider):
    name = "mofan"
    start_urls = [
        'https://myself-bbs.com/portal.php',
    ]
    # unseen = set()
    # seen = set()      # we don't need these two as scrapy will deal with them automatically

    def parse(self, response):
        yield {     # return some results
            'id': response.css('id::portal_block_951_content').extract_first(default='Missing').strip().replace('"', ""),
            'url': response.url,
        }

        urls = response.css('a::attr(href)').re(
            r'^/.+?/$')     # find all sub urls
        for url in urls:
            yield response.follow(url, callback=self.parse)
