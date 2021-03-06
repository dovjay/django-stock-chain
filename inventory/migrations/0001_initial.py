# Generated by Django 3.0.4 on 2020-03-26 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sku', models.CharField(max_length=200, unique=True)),
                ('sell_price', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('buy_price', models.PositiveIntegerField(default=0)),
                ('note', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('last_modified', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='inventory.Category')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Contact')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='Varian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(choices=[('WARNA', 'Warna'), ('UKURAN', 'Ukuran'), ('BERAT', 'Berat')], default='UKURAN', max_length=10)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VarianProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Product')),
                ('varian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Varian')),
            ],
        ),
    ]
