# Generated by Django 3.1.2 on 2020-11-21 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20201120_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
