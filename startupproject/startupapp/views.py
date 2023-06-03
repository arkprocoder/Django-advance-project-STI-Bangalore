from django.shortcuts import render,redirect
from authapp.models import Contact
from django.contrib import messages
from startupapp.models import Courses,Register,Payments
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

def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login & Register with us")
        return redirect("/auth/login/")
    courses=Courses.objects.all()
    context={"courses":courses}
# if the form is submitted this below logic is going to work 


    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        fatherName=request.POST.get('fatherName')
        phone=request.POST.get('phone')
        alternateNumber=request.POST.get('alternateNumber')
        email=request.POST.get('email')
        college=request.POST.get('college')
        addr=request.POST.get('addr')
        landmark=request.POST.get('landmark')
        street=request.POST.get('street')
        pcode=request.POST.get('pcode')
        city=request.POST.get('city')
        companyname=request.POST.get('companyname')
        Designation=request.POST.get('Designation')
        Qualification=request.POST.get('Qualification')
        cknowledge=request.POST.get('cknowledge')
        scourse=request.POST.get('scourse')
        ccourse=request.POST.get('ccourse')
        emailPresent=Register.objects.filter(email=email)
        if emailPresent:
            messages.error(request,"Email is already Taken")
            return redirect('/enroll/')

        if scourse==ccourse:
            pass
        else:
            messages.error(request,"Please Select the Valid Course...")
            return redirect('/enroll/')
        query=Register(firstName=fname,lastName=lname,fatherName=fatherName,phoneNumber=phone,alternateNumber=alternateNumber,email=email,collegeName=college,address=addr,landmark=landmark,street=street,city=city,pincode=pcode,companyName=companyname,designation=Designation,qualification=Qualification,computerKnowledge=cknowledge,Course=scourse)
        # print(query.candidateId)
        query.save()
        messages.success(request,"Enrollment Success")
        return redirect('/candidateprofile/')



    return render(request,"enroll.html",context)



def candidateprofile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login & View Your Profile")
        return redirect("/auth/login/")   
    currentuser=request.user.username
    print(currentuser)
    details=Register.objects.filter(email=currentuser)
    payment=Payments.objects.all()
    paymentstatus=""
    amount=0
    balance=0
    for j in payment:
        if str(j.name)==currentuser :
            # print(j.name,type(str(j.name)))
            # print('matching')
            paymentstatus=j.status
            amount=j.amountPaid
            balance=j.balance

    # print(paymentstatus)
    # print(amount)
    # print(balance)
    # print(details)
    paymentstats={"paymentstatus":paymentstatus,"amount":amount,"balance":balance}

    # attendanceStats=Attendace.objects.filter(email=currentuser)   
    # context={"details":details,"status":paymentstats,"attendanceStats":attendanceStats}
    context={"details":details,"status":paymentstats}
    print(context)
    return render(request,"profile.html",context)