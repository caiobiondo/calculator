# Generated by Django 2.2.9 on 2022-01-19 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CalculatorIrarocAPI', '0002_delete_calculoscombinada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculoscombinada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('ids_calc', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
            options={
                'verbose_name': 'Calculoscombinada',
                'verbose_name_plural': 'Calculoscombinadas',
            },
        ),
    ]
