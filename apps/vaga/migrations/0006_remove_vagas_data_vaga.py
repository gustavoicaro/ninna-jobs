# Generated by Django 4.1.2 on 2022-10-07 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaga', '0005_vagas_data_vaga'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vagas',
            name='data_vaga',
        ),
    ]
