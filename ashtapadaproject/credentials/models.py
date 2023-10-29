from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# class Students(models.Model):
#     name=models.CharField(max_length=100)
#     index=models.IntegerField(max_length=1001)
#     last_payment_date=models.DateTimeField()
#     next_payment_date=models.DateTimeField()
#     age=models.IntegerField(max_length=100)
#     address=models.CharField(max_length=200)
#     phone=models.CharField(max_length=20)
#     email=models.EmailField(max_length=100)
#     parant=models.CharField(max_length=100)
#     parantphone=models.CharField(max_length=20)


class Enquire(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phonenumbers=models.CharField(max_length=100)
    highedu=models.CharField(max_length=100)
    course=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Additional(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    eduqual=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    sq=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)