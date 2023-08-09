# Generated by Django 4.2.2 on 2023-07-19 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0003_cliente_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='foto_articulo',
            field=models.ImageField(blank=True, null=True, upload_to='articulos/fotos_perfil'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='foto_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='clientes/fotos_perfil'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='precio',
            field=models.IntegerField(),
        ),
    ]