# Generated by Django 4.1.2 on 2022-11-16 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('biografia', models.TextField()),
                ('libros', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('terror', 'terror'), ('romance', 'romance'), ('drama', 'drama'), ('comics', 'comics'), ('ficcion', 'ficcion'), ('infantil', 'infantil'), ('historia', 'historia'), ('juvenil', 'juvenil')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField()),
                ('paginas', models.IntegerField()),
                ('sinopsis', models.TextField()),
                ('genero', models.CharField(max_length=40)),
            ],
        ),
    ]