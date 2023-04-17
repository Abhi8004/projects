from django.db import models

# Create your models here.
class Book(models.Model):
    eno=models.IntegerField()
    etitle=models.CharField(max_length=64)
    eaut=models.CharField(max_length=64)
    edate=models.IntegerField(max_length=64)

    def __str__(self):
        return self.etitle
