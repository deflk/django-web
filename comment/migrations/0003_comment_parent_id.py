# Generated by Django 2.0.4 on 2018-05-14 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20180514_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent_id',
            field=models.IntegerField(default=0),
        ),
    ]
