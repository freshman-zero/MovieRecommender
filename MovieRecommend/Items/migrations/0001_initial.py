# Generated by Django 2.1.8 on 2020-05-15 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MovieTitle', models.CharField(max_length=100, verbose_name='电影名称')),
                ('Cover', models.URLField(verbose_name='链接')),
                ('StoryLine', models.TextField(blank=True, null=True, verbose_name='电影简介')),
            ],
        ),
    ]