# Generated by Django 3.1.2 on 2020-11-03 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayz_app', '0016_auto_20201103_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('magnitude', models.CharField(choices=[('x2.5', 'x2.5'), ('x3', 'x3'), ('x4', 'x4'), ('x5', 'x5'), ('x6', 'x6'), ('x7', 'x7'), ('x8', 'x8'), ('x12', 'x12'), ('x25', 'x25'), ('Other', 'Other')], default='Magnitude not defined', max_length=64)),
                ('sell_price', models.PositiveIntegerField()),
                ('buy_price', models.PositiveIntegerField(blank=True, default='Not provided', null=True)),
                ('scopes', models.ManyToManyField(to='dayz_app.Weapon')),
            ],
        ),
    ]
