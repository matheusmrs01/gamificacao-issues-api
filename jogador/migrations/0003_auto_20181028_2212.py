# Generated by Django 2.1.1 on 2018-10-29 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jogador', '0002_auto_20181028_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missao',
            name='jogador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Jogador', to='jogador.Jogador'),
        ),
    ]