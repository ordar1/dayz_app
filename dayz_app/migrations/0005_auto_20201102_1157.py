# Generated by Django 3.1.2 on 2020-11-02 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayz_app', '0004_auto_20201102_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='cal',
            field=models.CharField(choices=[('.308', '.308)'), ('7.62x54', '7.62x54'), ('7.62x39', '7.62x39'), ('5.56x45', '5.56x45'), ('5.45x39', '5.45x39'), ('12ga', '12ga'), ('.357', '.357'), ('9mm', '9mm'), ('.338', '.338'), ('.408', '.408'), ('.50', '.50')], default='Caliber not defined', max_length=60),
        ),
    ]
