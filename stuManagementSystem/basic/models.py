from django.db import models

# Create your models here.

class Admission_Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    father_name  = models.CharField(max_length=50)
    mothers_name  = models.CharField(max_length=50)
    grade_value  = models.FloatField(max_length=3)
    review  = models.TextField(max_length=500)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    