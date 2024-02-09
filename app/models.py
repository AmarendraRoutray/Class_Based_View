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