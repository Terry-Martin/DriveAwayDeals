# Generated by Django 4.2.16 on 2024-12-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0011_alter_transaction_transaction_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]