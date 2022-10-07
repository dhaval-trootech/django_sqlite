# Generated by Django 4.1.1 on 2022-10-04 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0020_alter_student_stud_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stud_role',
            field=models.CharField(choices=[('Python Dev', 1), ('React Dev', 2), ('PHP Dev', 3)], default='None', max_length=40),
        ),
    ]