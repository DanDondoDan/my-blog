from django.db import models

class Article(models.Model):
    header = models.CharField(max_length=500)
    content = models.TextField(max_length=10000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return '/blog/%i/' % self.id