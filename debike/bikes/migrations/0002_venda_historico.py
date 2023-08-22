# Generated by Django 4.2.4 on 2023-08-21 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bikes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_venda', models.DateTimeField(auto_now_add=True)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikes.bike')),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donos', models.TextField(default='[]')),
                ('vendas', models.TextField(default='[]')),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikes.bike')),
            ],
        ),
    ]
