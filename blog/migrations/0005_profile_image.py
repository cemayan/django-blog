# Generated by Django 2.0.4 on 2018-05-01 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180427_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.TextField(null=True),
        ),
    ]
