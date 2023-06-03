from django.contrib import admin
from startupapp.models import Courses,Trainer,Register,Payments
# Register your models here.
admin.site.register(Courses)
admin.site.register(Trainer)
admin.site.register(Register)
admin.site.register(Payments)