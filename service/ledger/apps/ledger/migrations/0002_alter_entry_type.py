# Generated by Django 4.2 on 2023-05-30 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Debit'), (1, 'Credit')], verbose_name='Type'),
        ),
    ]
