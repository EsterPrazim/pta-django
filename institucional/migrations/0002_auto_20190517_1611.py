# Generated by Django 2.2.1 on 2019-05-17 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institucional', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institucional',
            name='AutorInstitute',
        ),
        migrations.RemoveField(
            model_name='institucional',
            name='FraseInstitute',
        ),
    ]
