# Generated by Django 2.2.1 on 2019-12-14 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_indexsliderimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='artimage',
            name='author',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]