# Generated by Django 3.2.6 on 2021-08-19 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210819_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booster',
            name='regions',
            field=models.CharField(choices=[('EUNE', 'EUNE'), ('EUW', 'EUW'), ('NA', 'NA'), ('RU', 'RU'), ('TR', 'TR')], max_length=30),
        ),
    ]