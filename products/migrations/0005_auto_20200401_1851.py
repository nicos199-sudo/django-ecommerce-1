# Generated by Django 2.2.11 on 2020-04-01 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200401_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3),
        ),
    ]
