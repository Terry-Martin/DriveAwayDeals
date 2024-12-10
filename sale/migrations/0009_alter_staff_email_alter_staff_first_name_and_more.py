# Generated by Django 4.2.16 on 2024-12-10 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0008_rename_customerdetail_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='email',
            field=models.EmailField(max_length=60),
        ),
        migrations.AlterField(
            model_name='staff',
            name='first_name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.CharField(choices=[('salesperson', 'SALESPERSON'), ('manager', 'MANAGER')], default='salesperson', max_length=11),
        ),
        migrations.AlterField(
            model_name='staff',
            name='second_name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]