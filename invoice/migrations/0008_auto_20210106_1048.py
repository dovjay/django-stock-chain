# Generated by Django 3.0.7 on 2021-01-06 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0007_auto_20200507_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='discount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
