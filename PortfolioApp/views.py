from django.shortcuts import render , redirect
from .models import Education , WorkExperience , Projects , ContactUs

# Create your views here.

def index(request):
    
    return render(request , 'home.html')



def projects(request):
    return render(request , 'projects.html')  



def onepage(request):
    if request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('email')

        contact = ContactUs(name=name, email=email, message=message)
        contact.save()
    education = Education.objects.all()
    work_experience = WorkExperience.objects.all()
    projects = Projects.objects.all()

    context = {
        "education" : education,
        "work_experience" : work_experience ,
        "projects" : projects
    }
    return render(request , 'onepage.html' , context)      
