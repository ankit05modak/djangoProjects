from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.CharField(max_length=100)
    book_title = models.CharField(max_length=200)
    book_subtitle = models.CharField(max_length=200)
    book_authors = models.CharField(max_length=200)    # Multiple authers seperated by ,
    book_publisher = models.CharField(max_length=100)
    book_publishdate = models.DateField()
    book_category = models.CharField(max_length=100)
    book_distexpense = models.FloatField()

    def __str__(self):
        return self.book_title

