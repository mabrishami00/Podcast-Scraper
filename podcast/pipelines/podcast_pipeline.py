import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'Config.settings'
django.setup()


class PodcastPipeline:
    def process_item(self, item, spider):
        from main_app.models import Podcast
        
        Podcast.objects.create(
            title=item['title'],
            description=item['description'],
            audio_url=item['audio_url'],
            image_url=item['image_url'],
            duration=item['duration'],
            episode_number=item['episode_number'],
            episode_type=item['episode_type'],
            pub_date=item['pub_date']
        )
        return item