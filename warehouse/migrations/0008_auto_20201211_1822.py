# Generated by Django 3.1.3 on 2020-12-11 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0007_auto_20201210_2034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_id',
            new_name='id',
        ),
    ]
