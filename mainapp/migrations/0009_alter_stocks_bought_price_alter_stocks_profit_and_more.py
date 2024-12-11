# Generated by Django 4.0.5 on 2023-10-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_stocks_bought_price_alter_stocks_profit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='bought_price',
            field=models.FloatField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='profit',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='sold_price',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
    ]