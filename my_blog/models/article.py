from django.db import models
from my_blog.models.base import BaseModel

class Article(BaseModel):
    user = models.OneToOneField('User', on_delete=models.CASCADE,
                                related_name='%(class)s',
                                related_query_name='%(class)s'
                                )
    header = models.CharField(max_length=500)
    content = models.TextField(max_length=10000)
    
    def __str__(self):
        return self.header
