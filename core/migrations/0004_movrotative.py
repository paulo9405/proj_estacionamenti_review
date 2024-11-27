# Generated by Django 3.2.25 on 2024-11-27 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_marca_veiculo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovRotative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateTimeField()),
                ('checkout', models.DateTimeField(blank=True, null=True)),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pago', models.BooleanField(default=False)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.veiculo')),
            ],
        ),
    ]
