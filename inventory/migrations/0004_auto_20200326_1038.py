# Generated by Django 3.0.4 on 2020-03-26 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('inventory', '0003_auto_20200326_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Contact'),
        ),
    ]
