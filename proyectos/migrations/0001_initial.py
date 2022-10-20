# Generated by Django 4.1.2 on 2022-10-20 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('tecnologia', models.CharField(max_length=200)),
                ('creado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
