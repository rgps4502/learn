import scrapy


class MofanSpider(scrapy.Spider):
    name = "mofanSpider"
    start_urls = [
        'https://mofanpy.com/',
    ]
    # unseen = set()
    # seen = set()      # we don't need these two as scrapy will deal with them automatically

    def parse(self, response):
        yield {     # return some results
            'title': response.css('h1::text').extract_first(default='Missing').strip().replace('"', ""),
            'url': response.url,
        }

        urls = response.css('a::attr(href)').re(
            r'^/.+?/$')     # find all sub urls
        for url in urls:
            # it will filter duplication automatically
            yield response.follow(url, callback=self.parse)
