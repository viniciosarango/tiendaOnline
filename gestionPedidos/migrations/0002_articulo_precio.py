# Generated by Django 4.2.2 on 2023-07-05 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='precio',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
