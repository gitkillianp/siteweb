# Generated by Django 3.1.6 on 2023-05-08 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formulaire', '0002_auto_20230508_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formulairemodel',
            old_name='Numéro_de_telephone',
            new_name='Numéro_de_téléphone',
        ),
    ]