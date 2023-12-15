from django.shortcuts import render
from apps.settings.models import *
# Create your views here.
def index(request):
    about = About.objects.latest('id')
    settings = Settings.objects.latest('id')
    employee = Employee.objects.latest('id')
    slide = Slide.objects.all()
    ser = Servides.objects.all()
    rev = Reviews.objects.all()
    blog = Blogs.objects.all()    
    project = Project.objects.all()    
    return render(request, 'index-slideshow.html', locals())

def blog(request):
    return render(request, 'blog.html', locals())