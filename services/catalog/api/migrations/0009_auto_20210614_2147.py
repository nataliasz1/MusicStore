# Generated by Django 2.2.13 on 2021-06-14 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210610_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='catalog_item_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.CatalogItem'),
        ),
    ]