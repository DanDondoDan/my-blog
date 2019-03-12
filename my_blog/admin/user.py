
from django.contrib import admin
from my_blog import models
from my_blog.admin.base import BaseForm
import django.forms as forms


class UserAdminForm(BaseForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ('email', 'password')


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm