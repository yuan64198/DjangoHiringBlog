# Generated by Django 3.1.2 on 2020-10-26 03:36

from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('location', localflavor.us.models.USStateField(blank=True, default=('AL', 'Alabama'), max_length=2, null=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('expected_salary', models.IntegerField()),
                ('will_relocate', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('apply_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
    ]
