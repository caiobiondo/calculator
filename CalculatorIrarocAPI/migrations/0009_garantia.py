# Generated by Django 2.2 on 2022-01-26 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CalculatorIrarocAPI', '0008_garantiabem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Garantia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('instrumento', models.CharField(default='', max_length=50)),
                ('bem', models.CharField(default='', max_length=50)),
                ('natureza', models.CharField(default='', max_length=50)),
            ],
            options={
                'verbose_name': 'Garantia',
                'verbose_name_plural': 'Garantias',
            },
        ),
    ]