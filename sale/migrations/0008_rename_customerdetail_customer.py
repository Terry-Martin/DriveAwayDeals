# Generated by Django 4.2.16 on 2024-12-10 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0007_alter_customerdetail_updated_by'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomerDetail',
            new_name='Customer',
        ),
    ]
