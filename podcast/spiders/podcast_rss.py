import scrapy


class PodcastRssSpider(scrapy.Spider):
    name = "podcast_rss"
    allowed_domains = ["google.com"]
    start_urls = ["https://google.com"]

    def parse(self, response):
        pass
