import django.forms as forms


class BaseForm(forms.ModelForm):
    class Meta:
        exclude = ('created', 'changed')