# Generated by Django 5.0.2 on 2024-03-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_userprofile_options_alter_userprofile_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='funds',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='money_invested',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pnl',
            field=models.IntegerField(default=0),
        ),
    ]
