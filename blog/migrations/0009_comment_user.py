# Generated by Django 2.0.4 on 2018-05-07 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180507_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=None, to='blog.Profile', to_field='user'),
        ),
    ]