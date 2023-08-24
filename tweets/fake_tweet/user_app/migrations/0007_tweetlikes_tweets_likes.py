# Generated by Django 4.2 on 2023-08-17 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_app', '0006_remove_tweets_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.BooleanField(default=False, verbose_name='Beğendi mi')),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.tweets', verbose_name='Tweet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.AddField(
            model_name='tweets',
            name='likes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_app.tweetlikes', verbose_name='Beğeniler'),
        ),
    ]
