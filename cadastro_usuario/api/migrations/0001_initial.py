# Generated by Django 4.0.3 on 2022-03-23 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=40, verbose_name='LOGIN')),
                ('senha', models.CharField(max_length=40, null=True, verbose_name='SENHA')),
                ('data_nascimento', models.DateField(verbose_name='DATA_NASCIMENTO')),
            ],
        ),
    ]
