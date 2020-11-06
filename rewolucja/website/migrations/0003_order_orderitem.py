# Generated by Django 3.1.2 on 2020-11-06 20:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20201105_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, verbose_name='Imie')),
                ('last_name', models.CharField(blank=True, max_length=200, verbose_name='Nazwisko')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Dozwolony format numeru telefonu: '+999999999'. Do 15 cyfr.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Numer Telefonu')),
                ('address_line_1', models.CharField(blank=True, max_length=200, verbose_name='Adres linia 1')),
                ('address_line_2', models.CharField(blank=True, max_length=200, null=True, verbose_name='Adres linia 2')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='Miasto')),
                ('zip_code', models.CharField(blank=True, max_length=30, verbose_name='Kod pocztowy')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='Kraj')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data aktualizacji')),
                ('sent', models.BooleanField(default=False, verbose_name='Wysłane')),
                ('paid', models.BooleanField(default=False, verbose_name='Zapłacone')),
            ],
            options={
                'verbose_name': 'Zamówienie',
                'verbose_name_plural': 'Zamówienia',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='website.order', verbose_name='Zamówienie')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='website.product', verbose_name='Produkt')),
            ],
        ),
    ]
