from scrapy.item import Item, Field


class PodcastItem(Item):
    title = Field(
        input_processors=MapCompose(str.strip, remove_tags),
        output_processor=TakeFirst()
    )
    description = Field(
        input_processor=MapCompose(str.strip, remove_tags),
        output_processor=TakeFirst()
    )
    pub_date = Field(output_processor=TakeFirst())
    audio_url = Field(output_processor=TakeFirst())
    duration = Field(output_processor=TakeFirst())