# Generated by Django 4.2.16 on 2024-12-21 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0012_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='updated_by_who', to='sale.staff'),
        ),
    ]
