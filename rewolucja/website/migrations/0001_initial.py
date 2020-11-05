# Generated by Django 3.1.2 on 2020-11-05 09:04

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, verbose_name='Tytuł')),
                ('content', models.FileField(upload_to='uploads/newsletters', verbose_name='Zawartość (Plik HTML)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data aktualizacji')),
            ],
            options={
                'verbose_name': 'Newsletter',
                'verbose_name_plural': 'Newslettery',
                'ordering': ('created_at', 'title'),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, verbose_name='Nazwa')),
                ('description', models.TextField(blank=True, verbose_name='Opis')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cena')),
                ('available', models.BooleanField(default=True, verbose_name='Dostępność')),
                ('stock', models.PositiveIntegerField(verbose_name='Ilość')),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data aktualizacji')),
            ],
            options={
                'verbose_name': 'Produkt',
                'verbose_name_plural': 'Produkty',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, verbose_name='Nazwa Kategorii/Kolekcji')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Opis(Opcjonalnie)')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data aktualizacji')),
            ],
            options={
                'verbose_name': 'Kategoria Produktu',
                'verbose_name_plural': 'Kategorie Produktów',
                'ordering': ('name', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('conf_num', models.CharField(max_length=15)),
                ('confirmed', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Subskrybent Newsletteru',
                'verbose_name_plural': 'Subskrybenci Newsletteru',
            },
        ),
        migrations.CreateModel(
            name='ProductOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('NO SIZE', 'Brak rozmiaru'), ('universal', 'Uniwersalny')], max_length=100, verbose_name='Rozmiar produktu')),
                ('stock', models.PositiveIntegerField()),
                ('sold_out', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='website.product', verbose_name='Produkt')),
            ],
            options={
                'verbose_name': 'Opcje produktu',
                'verbose_name_plural': 'Opcje produktów',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='website.product')),
            ],
            options={
                'verbose_name': 'Zdjęcie produktu',
                'verbose_name_plural': 'Zdjęcia produktów',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category', to='website.productcategory', verbose_name='Kategoria'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Tytuł')),
                ('subtitle', models.TextField(blank=True, null=True, verbose_name='Podtytuł(Opcjonalnie)')),
                ('text', models.TextField(verbose_name='Treść Posta')),
                ('image', models.ImageField(upload_to='uploads/articles/thumbnails', verbose_name='Zdjęcie')),
                ('status', models.CharField(choices=[('draft', 'Wstrzymaj'), ('published', 'Opublikuj')], default='draft', max_length=100, verbose_name='Status publikacji')),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('hits', models.IntegerField(default=0, editable=False, verbose_name='Wyświetlenia')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data aktualizacji')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tagi')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posty',
                'ordering': ['-created_at', 'updated_at'],
            },
        ),
        migrations.CreateModel(
            name='ArtItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Tytuł')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Opis(Opcjonalnie')),
                ('author', models.CharField(blank=True, max_length=256, null=True)),
                ('image', models.ImageField(upload_to='uploads/art/images', verbose_name='Zdjęcie')),
                ('visible', models.BooleanField(default=True, verbose_name='Wyświetlaj')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data utworzenia')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data aktualizacji')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tagi')),
            ],
            options={
                'verbose_name': 'Sztuka',
                'verbose_name_plural': 'Sztuka',
                'ordering': ['-created_at', 'updated_at'],
            },
        ),
    ]
