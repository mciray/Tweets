# Generated by Django 4.2 on 2023-08-10 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='image',
            field=models.FileField(blank=True, upload_to='Uploads', verbose_name='Dosya'),
        ),
    ]