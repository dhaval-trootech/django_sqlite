# Generated by Django 4.1 on 2022-09-23 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0011_alter_student_stud_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='stud_id',
            new_name='stud_ids',
        ),
    ]
