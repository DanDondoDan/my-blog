from django.db import models
from my_blog.models.base import BaseModel
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from my_blog.models.user import User

class ArticleManager(models.Manager):
    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().order_by('-date')

class Article(BaseModel):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
                                
    header = models.CharField(max_length=500)
    content = models.TextField(max_length=10000)

    objects = ArticleManager()

    
    def __str__(self):
        return self.header

    def get_subs_emails(self):
        
        emails = self.user.subscribers.subscribers.values_list('email', flat=True)
        

    def send_notification(self):
            site = Site.objects.get_current()
            html = render_to_string('my_blog/email/notification.txt', context={'post': self, 'site_url': site.domain})
            body = render_to_string('my_blog/email/notification.html', context={'post': self, 'site_url': site.domain})
            recipients = self.get_subs_emails()
            return send_mail('New post %s' % site.name, body, recipients, html_message=html)
                

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subscribers')
                                
    subscribers = models.ManyToManyField('User')


class ArticleRead(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'user')



