from django.contrib import admin
from .models import tbl_login,tbl_registration,Enquiry,Upload_Study,Upload_Lecture,Upload_Asmt,Noti
# Register your models here.
admin.site.register(tbl_registration)
admin.site.register(Enquiry)
admin.site.register(Upload_Study)
admin.site.register(Upload_Lecture)
admin.site.register(Upload_Asmt)
admin.site.register(tbl_login)
admin.site.register(Noti)

