# Generated by Django 3.1.2 on 2020-10-24 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201024_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comparny_name',
            field=models.CharField(default='Nan', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(default='Nan', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='salary',
            field=models.CharField(default='0 K', max_length=100),
        ),
    ]
