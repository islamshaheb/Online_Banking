# Generated by Django 2.2 on 2019-07-26 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_auto_20190725_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banker',
            old_name='User_name',
            new_name='Banker_name',
        ),
    ]
