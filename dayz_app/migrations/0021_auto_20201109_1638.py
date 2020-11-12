# Generated by Django 3.1.2 on 2020-11-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayz_app', '0020_auto_20201109_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='scopes',
            field=models.ManyToManyField(blank=True, default='No scope provided', related_name='weapon_scopes', to='dayz_app.Scope'),
        ),
    ]