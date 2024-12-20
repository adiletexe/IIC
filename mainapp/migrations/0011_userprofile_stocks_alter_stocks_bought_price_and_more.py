# Generated by Django 4.2.1 on 2024-11-30 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0010_remove_userprofile_stocks_alter_stocks_bought_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='stocks',
            field=models.ManyToManyField(blank=True, to='mainapp.stocks'),
        ),
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
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='sold_price',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='state',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='title',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='balance',
            field=models.FloatField(default=1000000, max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
