# Generated by Django 3.1.5 on 2021-01-15 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_carros_data_de_nascimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='carros',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='carros',
            name='data_de_nascimento',
            field=models.CharField(max_length=10),
        ),
    ]