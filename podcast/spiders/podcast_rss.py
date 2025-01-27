from scrapy.spiders import XMLFeedSpider


class PodcastRssSpider(XMLFeedSpider):
    name = "podcast_rss"
    allowed_domains = ["acast.com"]
    start_urls = ["https://feeds.acast.com/public/shows/65e095ffbec0f30016047f7e"]
    
    iterator = 'iternodes'
    itertag = 'item'  
    
    namespaces = [
        ('itunes', 'http://www.itunes.com/dtds/podcast-1.0.dtd'),
    ]
    
    def parse_node(self, response, node):
        """Extract data from each podcast episode"""
        yield {
            'title': node.xpath('.//title/text()').get(),
            'description': node.xpath('.//description/text()').get(),
            'pub_date': node.xpath('.//pubDate/text()').get(),
            'duration': node.xpath('.//itunes:duration/text()', namespaces=self.namespaces).get(),
            'audio_url': node.xpath('.//enclosure/@url').get(),
            'episode_type': node.xpath('.//itunes:episodeType/text()', namespaces=self.namespaces).get(),
            'episode_number': node.xpath('.//itunes:episode/text()', namespaces=self.namespaces).get(),
            'image': node.xpath('.//itunes:image/@href', namespaces=self.namespaces).get(),
        }