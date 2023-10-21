from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    parentsName = models.CharField(max_length=50)
    dOb = models.DateField()
    favSubject = models.CharField(max_length=50)
    typ = models.CharField(max_length=10, default="Regular")
    
    def __str__(self) -> str:
        return self.name