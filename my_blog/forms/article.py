from django import forms

from my_blog.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('header', 'context')