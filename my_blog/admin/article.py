from django.contrib import admin
from my_blog import models
from my_blog.admin.base import BaseForm


class ArticleAdminForm(BaseForm):
    class Meta:
        model = models.Article
        exclude = BaseForm.Meta.exclude


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ('header',
                    'content',
                    )