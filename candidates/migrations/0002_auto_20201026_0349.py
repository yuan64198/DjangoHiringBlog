# Generated by Django 3.1.2 on 2020-10-26 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='location',
            new_name='state',
        ),
    ]
