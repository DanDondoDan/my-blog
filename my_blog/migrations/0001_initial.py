# Generated by Django 2.1.4 on 2019-03-12 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=500)),
                ('content', models.TextField(max_length=10000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]