# Generated by Django 4.1 on 2022-09-22 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0009_alter_student_stud_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stud_name',
            field=models.CharField(choices=[('1', 'Dhaval'), ('2', 'Jaydip'), ('3', 'Jaymeet'), ('4', 'Sagar'), ('5', 'Karan'), ('6', 'Ajit')], max_length=55),
        ),
    ]