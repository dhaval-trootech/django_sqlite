from django.db import models


# Create your models here.
class Student(models.Model):
    DATA_CHOICE = [('Python Dev', 1), ('React Dev', 2), ('PHP Dev', 3)]
    stud_id = models.IntegerField(verbose_name='STUD_ID')
    stud_name = models.CharField(max_length=255, default='None',)
    stud_role = models.CharField(max_length=40, choices=DATA_CHOICE, default='None')
    stud_address = models.CharField(max_length=25, verbose_name='Hometown')
    stud_phone = models.IntegerField()
