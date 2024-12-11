# Generated by Django 4.2.1 on 2024-11-30 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0009_alter_stocks_bought_price_alter_stocks_profit_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='stocks',
        ),
        migrations.AlterField(
            model_name='stocks',
            name='bought_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='profit',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='sold_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='state',
            field=models.CharField(choices=[('active', 'Active'), ('sold', 'Sold')], default='active', max_length=10),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='title',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='balance',
            field=models.FloatField(default=1000000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]