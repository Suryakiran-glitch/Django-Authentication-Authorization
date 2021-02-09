from django.db import models


# Create your models here.
class Usermodel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=50,blank=False)
    role = models.CharField(max_length=50, default="subscriber")


