# Generated by Django 3.0.4 on 2020-04-02 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20200330_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Category'),
        ),
    ]
