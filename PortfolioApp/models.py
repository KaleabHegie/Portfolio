from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.CharField( max_length=500)


class Education(models.Model):
    school_type = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    description = models.CharField( max_length=500)   
    file = models.FileField(upload_to="", max_length=100 , null=True , blank=True) 
    date_start = models.DateField(auto_now=False, auto_now_add=False)
    date_end = models.DateField(auto_now=False, auto_now_add=False)
    

class WorkExperience(models.Model):
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=254)
    description = models.CharField( max_length=500)   
    file = models.FileField(upload_to="", max_length=100 ,  null=True , blank=True) 
    date_start = models.DateField(auto_now=False, auto_now_add=False)
    date_end = models.DateField(auto_now=False, auto_now_add=False)   



class Projects(models.Model):
    image = models.ImageField(upload_to="" ,  null=True , blank=True)
    title = models.CharField(max_length=50)
    description = models.CharField( max_length=500)   






    
