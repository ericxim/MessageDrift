# Generated by Django 3.0.8 on 2021-05-04 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_remove_communities_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='default title', max_length=30),
            preserve_default=False,
        ),
    ]