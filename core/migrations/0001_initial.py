# Generated by Django 4.0.2 on 2022-02-16 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sexo', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1, verbose_name='Sexo')),
                ('cpf', models.CharField(max_length=15, verbose_name='CPF')),
                ('nasc', models.DateField(max_length=8, verbose_name='Nascimento')),
                ('telefone', models.CharField(max_length=10, verbose_name='Telefone')),
                ('celular', models.CharField(max_length=11, verbose_name='Celular')),
            ],
        ),
    ]
