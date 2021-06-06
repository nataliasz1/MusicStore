# Generated by Django 2.2.13 on 2021-06-03 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210602_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogitem',
            name='description_long',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='catalogitem',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='catalogitem',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
