from django.db import models

# Create your models here.

class student(models.Model):
    stuid = models.IntegerField()
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)
    # this function show human readable data in database by using any attribute you can show now i use stuid,carefull this fun only return string type so conver studid in string using str
    # def __str__(self):
    #     return str(self.stuid)
   
    