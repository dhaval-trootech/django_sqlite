# Generated by Django 4.1 on 2022-09-20 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='papa',
            old_name='stud_addres',
            new_name='stud_address',
        ),
    ]