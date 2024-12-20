# Generated by Django 3.2.25 on 2024-11-27 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_movrotative'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensalista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField()),
                ('valor_mes', models.DecimalField(decimal_places=2, max_digits=6)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.veiculo')),
            ],
        ),
        migrations.CreateModel(
            name='MovMensalista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pagamento', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('mensalista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mensalista')),
            ],
        ),
    ]
