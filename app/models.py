from django.db import models

# Create your models here.



class Songs(models.Model):
    songname=models.CharField(max_length=100)
    singer = models.CharField(max_length=100)
    
    def __str__(self):
        return self.songname


class Whisky(models.Model):
    pname = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    
    
    
class School(models.Model):
    sname = models.CharField(max_length=100)
    sprincipal = models.CharField(max_length=100)
    slocation = models.CharField(max_length=100)
    
class Student(models.Model):
    stuname = models.CharField(max_length=100)
    stuage = models.IntegerField()
    sname = models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')