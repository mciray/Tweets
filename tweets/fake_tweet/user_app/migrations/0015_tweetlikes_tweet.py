# Generated by Django 4.2 on 2023-08-22 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0014_remove_tweetlikes_tweet'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetlikes',
            name='tweet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_app.tweets', verbose_name='Beğenilen Post'),
        ),
    ]
