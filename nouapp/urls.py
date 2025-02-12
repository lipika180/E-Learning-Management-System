
from django.urls import path,include
from.views import*
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('',home,name="home"),
   path('about',about,name="about"),
    path('login',login,name="login"),
   path('contact',contact,name="contact"),
   path('logcode',logcode,name="logcode"),
   path('registration',registration,name="reg"),
   path('logout',logout,name="logout"),
   path('adminzone',adminzone,name="adminzone"),
   path('show_students',show_students,name="show_students"),
   path('adminhome',adminhome,name="adminhome"),
   path('usm',usm,name="usm"),
   path('uplec',uplec,name="uplec"),
   path('uplec',uplec,name="uplec"),
   path('upass',upass,name="upass"),
   path('noti',add_notification,name="noti"),
   

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
