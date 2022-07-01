from django.db import models

# Create your models here.
class room(models.Model):
	date=models.DateTimeField()
	title=models.CharField(max_length=200)
	content=models.CharField(max_length=5000)
	types=models.CharField(max_length=100)
class project(models.Model):
	title=models.CharField(max_length=200)
	content=models.CharField(max_length=5000)
	project_Main_Img = models.ImageField(upload_to='img/')
	details=models.CharField(max_length=200)
	fork=models.CharField(max_length=200)
class mail(models.Model):
	gmail=models.CharField(max_length=100)
	
    

    
