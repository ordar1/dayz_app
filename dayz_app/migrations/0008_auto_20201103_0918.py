# Generated by Django 3.1.2 on 2020-11-03 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayz_app', '0007_auto_20201102_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type_of_weapon',
            name='weapon',
            field=models.CharField(choices=[('Sniper rifle', 'Sniper rifle'), ('Shotgun', 'Shotgun'), ('Assault Rifle', 'Assault Rifle'), ('Machine Gun', 'Machine Gun')], default='Weapon type not defined', max_length=60),
        ),
    ]