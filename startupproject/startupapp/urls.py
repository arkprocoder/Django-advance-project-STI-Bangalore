from django.urls import path
from startupapp import views


urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('courses/',views.courses,name="courses"),
    path('course/<id>/',views.course,name="course"),
    path('enroll/',views.enroll,name="enroll"),
    path('candidateprofile/',views.candidateprofile,name="candidateprofile"),
    path('candidateupdate/<id>/',views.candidateupdate,name="candidateupdate"),
    path('attendance/',views.attendance,name="attendance"),
    path('search/',views.search,name="search")

]
