# Generated by Django 4.1 on 2022-09-21 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0007_alter_student_stud_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stud_phone',
            field=models.IntegerField(),
        ),
    ]