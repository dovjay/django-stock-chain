# Generated by Django 3.0.4 on 2020-05-07 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20200414_1251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='varianproduct',
            old_name='varian_value',
            new_name='product_type',
        ),
        migrations.RemoveField(
            model_name='varianproduct',
            name='varian_attribute',
        ),
        migrations.AddField(
            model_name='varianproduct',
            name='size',
            field=models.CharField(choices=[('1-3', '1-3'), ('4-6', '4-6'), ('8-10', '8-10'), ('5-15', '5-15'), ('7-15', '7-15'), ('11-13', '11-13'), ('100-140', '100-140'), ('150-180', '150-180')], default='1-3', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default_product.jpg', upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=200),
        ),
    ]
