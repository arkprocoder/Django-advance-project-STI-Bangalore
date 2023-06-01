from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.
class Courses(models.Model):
    courseName=models.CharField(max_length=150,primary_key=True)
    image=models.ImageField(upload_to="course",blank=True,null=True)
    courseFee=models.IntegerField()
    courseDuration=models.IntegerField()
    syllabus=RichTextField(default="syllabus")
    aboutCourse=RichTextField(default="aboutCourse")
    stars=models.IntegerField(default=3)

    def __str__(self):
        return self.courseName