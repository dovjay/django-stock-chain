# Generated by Django 3.0.4 on 2020-04-02 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20200402_1221'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]
