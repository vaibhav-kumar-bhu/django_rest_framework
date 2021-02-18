from django.contrib import admin
from api.models import student
@admin.register(student)
class studentadmin(admin.ModelAdmin):
	list_display=['id','name','roll','age','state']

# Register your models here.
