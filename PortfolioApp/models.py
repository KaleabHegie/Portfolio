from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.CharField( max_length=500)

    def __str__(self):
        return self.name
    

class Education(models.Model):
    school_type = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    description = models.CharField( max_length=500)   
    file = models.FileField(upload_to="", max_length=100 , null=True , blank=True) 
    date_start = models.DateField(auto_now=False, auto_now_add=False)
    date_end = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.school_type
    

class WorkExperience(models.Model):
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=254)
    description = models.CharField( max_length=500)   
    file = models.FileField(upload_to="", max_length=100 ,  null=True , blank=True) 
    date_start = models.DateField(auto_now=False, auto_now_add=False)
    date_end = models.DateField(auto_now=False, auto_now_add=False)   

    def __str__(self):
        return self.company
    

project_type = {
    "React" : "react",
    "Django" : "django",
    "PHP" : "php",
    "Python" : "python",
    "JavaScript" : "javascript",

}

class Projects(models.Model):
    image = models.ImageField(upload_to="" ,  null=True , blank=True)
    project_type = models.CharField(choices=project_type , max_length=50 , null=True , blank=True)
    title = models.CharField(max_length=50)
    description = models.CharField( max_length=500)   


    def __str__(self):
        return self.title

    






    
