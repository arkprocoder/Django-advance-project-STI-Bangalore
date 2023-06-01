from django.shortcuts import render
from authapp.models import Contact
from django.contrib import messages
from startupapp.models import Courses
# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneNo=request.POST.get('num')
        desc=request.POST.get('desc')
        query=Contact(name=name,email=email,phoneNumber=phoneNo,description=desc)
        query.save()
        messages.success(request,"Thanks for Contacting us we will get back you soon...")
        return render(request,"contact.html")
    return render(request,"contact.html")


def courses(request):
    courses=Courses.objects.all()
    context={"courses":courses}
    return render(request,"courses.html",context)

def course(request,id):
    course=Courses.objects.filter(courseName=id)
    context={"course":course}
    return render(request,"course.html",context)

