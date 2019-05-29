from django.contrib import admin
from .models import Emp
# Register your models here.
class Emp_admin(admin.ModelAdmin):
    list_display=['id','emp_no','emp_name','emp_sal']

admin.site.register(Emp,Emp_admin)