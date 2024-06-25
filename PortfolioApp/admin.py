from django.contrib import admin
from .models import ContactUs , Education , WorkExperience , Projects
# Register your models here.

admin.site.register(ContactUs)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Projects)