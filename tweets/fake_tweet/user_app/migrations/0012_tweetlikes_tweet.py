# Generated by Django 4.2 on 2023-08-22 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0011_alter_tweets_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetlikes',
            name='tweet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_app.tweets', verbose_name='Beğendiği Tweet'),
        ),
    ]
