# Generated by Django 3.1.6 on 2021-02-24 16:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20210224_1121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_on']},
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='blog_content',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='user',
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='created_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
        migrations.AddField(
            model_name='blog',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
