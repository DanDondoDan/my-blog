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

class SubscriptionAdminForm(BaseForm):
    class Meta:
        model = models.Subscription
        exclude = BaseForm.Meta.exclude


@admin.register(models.Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    # list_display = ('subscrubers',)
                    
class ArticleReadAdminForm(BaseForm):
    class Meta:
        model = models.ArticleRead
        exclude = BaseForm.Meta.exclude


@admin.register(models.ArticleRead)
class ArticleReadAdmin(admin.ModelAdmin):
    form = ArticleReadAdminForm
    list_display = ('post',)
              