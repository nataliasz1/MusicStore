# Generated by Django 3.2.3 on 2021-05-31 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_payment_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='user_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]