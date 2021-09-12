# Generated by Django 3.2.6 on 2021-08-19 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_booster_orders_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booster',
            name='id_name',
        ),
        migrations.AlterField(
            model_name='account',
            name='is_booster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.booster'),
        ),
    ]
