from datetime import datetime
from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(default=datetime.now)
    changed = models.DateTimeField(auto_now=True)