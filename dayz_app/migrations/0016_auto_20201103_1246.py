# Generated by Django 3.1.2 on 2020-11-03 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayz_app', '0015_auto_20201103_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type_of_weapon',
            name='type',
            field=models.CharField(choices=[('Sniper rifle', 'Sniper rifle'), ('Shotgun', 'Shotgun'), ('Assault Rifle', 'Assault Rifle'), ('Machine Gun', 'Machine Gun')], default='Weapon type not defined', max_length=60),
        ),
    ]
