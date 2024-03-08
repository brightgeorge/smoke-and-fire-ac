from django.db import models

# Create your models here.
class login(models.Model):
    emp_id = models.CharField(max_length=100)
    emp_name = models.CharField(max_length=250)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=20)
    #emp_branch = models.CharField(max_length=200)
    emp_description = models.TextField()
    user_flage = models.IntegerField()