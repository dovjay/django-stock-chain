# Generated by Django 3.0.4 on 2020-05-07 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_auto_20200425_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Draft'), ('HUTANG', 'Hutang'), ('BAYAR', 'Bayar')], default='DRAFT', max_length=10),
        ),
    ]
