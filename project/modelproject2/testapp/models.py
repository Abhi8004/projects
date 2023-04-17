from django.db import models

# Create your models here.
class Job(models.Model):
    epost=models.IntegerField()
    elocat=models.CharField(max_length=64)
    esal=models.FloatField()
    equal=models.CharField(max_length=64)

    def __str__(self):
        return self.elocat
