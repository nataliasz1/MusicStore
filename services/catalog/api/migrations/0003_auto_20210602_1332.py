# Generated by Django 2.2.13 on 2021-06-02 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='catalog_item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.CatalogItem'),
        ),
    ]
