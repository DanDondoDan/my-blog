import threading

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from my_blog.models import Article, ArticleRead


@receiver(post_save, sender=Article)
def post_save_handler(sender, instance, created, **kwargs):
    if created:
        thread = threading.Thread(target=instance.send_notification)
        thread.start()