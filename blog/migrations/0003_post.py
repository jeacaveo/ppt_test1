# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 17:40
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
from utils.data import get_json_from_file 


def load_fixtures(apps, schema_editor):
    if settings.TESTING:
        return

    Author = apps.get_model("blog", "Author")
    Tag = apps.get_model("blog", "Tag")
    Post = apps.get_model("blog", "Post")
    data = get_json_from_file("posts.json")[1]
    for post in data.get("posts"):
        author, created = Author.objects.get_or_create(name=post.get("author"))
        post_obj = Post.objects.create(title=post.get("title"),
                                       description=post.get("description"),
                                       author=author)
        # Adding tags to post
        (post_obj.tags.add(Tag.objects.get_or_create(name=tag)[0])
         for tag in post.get("tags").split(", ")
         if post.get("tags"))


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Author')),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='blog.Tag')),
            ],
        ),
        migrations.RunPython(load_fixtures),
    ]
