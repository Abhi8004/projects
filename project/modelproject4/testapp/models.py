from django.db import models

# Create your models here.
class Customer(models.Model):
    ename=models.CharField(max_length=64)
    email=models.CharField(max_length=64)
    ephone=models.IntegerField()
    eaccount=models.IntegerField()
    eage=models.IntegerField()

    def __str__(self):
        return self.ename
