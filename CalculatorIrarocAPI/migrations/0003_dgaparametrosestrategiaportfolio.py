# Generated by Django 2.2 on 2022-01-26 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CalculatorIrarocAPI', '0002_auto_20220125_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dgaparametrosestrategiaportfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('cliente', models.CharField(default='', max_length=50)),
            ],
            options={
                'verbose_name': 'Dgaparametrosestrategiaportfolio',
                'verbose_name_plural': 'Dgaparametrosestrategiaportfolios',
            },
        ),
    ]
