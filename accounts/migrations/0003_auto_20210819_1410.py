# Generated by Django 3.2.6 on 2021-08-19 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_data_joined_account_date_joined'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
            ],
        ),
        migrations.CreateModel(
            name='Booster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=512)),
                ('rank', models.CharField(max_length=30)),
                ('roles', models.CharField(max_length=30)),
                ('champions', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=False)),
                ('reviews', models.IntegerField()),
                ('regions', models.CharField(max_length=30)),
                ('orders_done', models.IntegerField()),
                ('languages', models.CharField(choices=[('EN', 'English'), ('PL', 'Polish'), ('KR', 'Korean')], max_length=30)),
                ('id_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
