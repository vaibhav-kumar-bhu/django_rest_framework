from django.db import models

# Create your models here.
class student(models.Model):
	name=models.CharField(max_length=20)
	roll=models.IntegerField()
	age=models.IntegerField()
	state=models.CharField(max_length=20)
	
