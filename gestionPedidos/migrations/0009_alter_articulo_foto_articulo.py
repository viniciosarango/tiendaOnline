# Generated by Django 4.2.2 on 2023-07-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0008_articulo_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='foto_articulo',
            field=models.ImageField(blank=True, null=True, upload_to='articulos/fotos_articulo'),
        ),
    ]