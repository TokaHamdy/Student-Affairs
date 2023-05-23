from django.contrib import admin
from .models import *
# Register your models here.
class studentadmin(admin.ModelAdmin):
    list_display =['name','student_id','GPA','level','birthday','department','phonenumber','gender','State']
    list_editable=['student_id','GPA','level','birthday','department','phonenumber','gender','State']
    search_fields=['name','student_id','department']
    list_filter=['department']
admin.site.register(Add,studentadmin)
admin.site.site_header='Hello MR:Omar '
admin.site.site_title='Omar site'
