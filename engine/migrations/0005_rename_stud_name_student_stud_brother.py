# Generated by Django 4.1 on 2022-09-21 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0004_alter_student_stud_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='stud_name',
            new_name='stud_brother',
        ),
    ]