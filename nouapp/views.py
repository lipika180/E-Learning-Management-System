from django.shortcuts import render,HttpResponse,redirect
from.models import tbl_login,tbl_registration,Enquiry,Upload_Study,Upload_Lecture,Upload_Asmt,Noti
from django.contrib import messages
from django.utils import timezone
from django.views.decorators.cache import cache_control
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')
def contact(request):
    if request.method=="POST":
         name=request.POST['name']
         contactno=request.POST['contactno']
         email=request.POST['email']
         address=request.POST['address']
         enqtxt=request.POST['enqtxt']
         enqdate=timezone.now()
         ab=Enquiry(name=name,contactno=contactno,email=email,address=address,enqtxt=enqtxt,enqdate=enqdate)
         ab.save()
         messages.success(request,'Enquiry Save SuccessFully')
    return render(request, 'contact.html')

def logcode(request):
    if request.method=="POST":
        usertype=request.POST['usertype']
        username=request.POST['username']
        password=request.POST['password']
        user=tbl_login.objects.filter(username=username,password=password).first()
        if user:
            if user.usertype=="admin"and usertype=="admin":
                request.session['userid']=username
                return redirect('adminhome')
            elif user.usertype=="student" and usertype=="student":
                 return HttpResponse("dear student this page is comming soon")
            else:
                messages.success(request,"Your Type is Not Match")
                return redirect('login')
                
        else:   
                messages.success(request,"User Doesnt Valid")
                return redirect('login')
        
def registration(request):
        if request.method=="POST":
             rollno=request.POST['rollno']
             name=request.POST['name']
             fname=request.POST['fname']
             mname=request.POST['mname']
             gender=request.POST['gender']
             program=request.POST['program']
             branch=request.POST['branch']
             year=request.POST['year']
             mobile=request.POST['mobile']
             email=request.POST['email']
             password=request.POST['password']
             usertype="student"
             regdate=timezone.now()
             ab=tbl_registration(rollno=rollno,name=name,fname=fname,mname=mname,gender=gender,program=program,branch=branch,year=year,mobile=mobile,email=email,password=password,usertype=usertype,regdate=regdate)
             ba=tbl_login(username=email,password=password,usertype=usertype)
             ba.save()
             ab.save()
             messages.success(request,'Your registration is successfully done and please check your email for login id and password')
             
        return render(request, 'registration.html')
def logout(request):
     request.session.flush()
     return redirect('login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminzone(request):
     if 'userid' in request.session:
          return render(request,'adminzone.html')
     else:
          return redirect('login')
     
def show_students(request):
     ab=tbl_registration.objects.all()
     return render(request,'showstu.html',{'Show':ab})
def adminhome(request):
     return render(request,'adminhome.html')
def usm(request):
     sh=Upload_Study.objects.all()
     if request.method=="POST":
          program=request.POST['program']
          branch=request.POST['branch']
          year=request.POST['year']
          subject=request.POST['subject']
          new_file=request.FILES['new_file']
          file_update=timezone.now()
          ab=Upload_Study(program=program,branch=branch,year=year,subject=subject,new_file=new_file,file_update=file_update)
          ab.save()
          messages.success(request,'File Upload Successfully')
          return redirect('usm')



     
def uplec(request):
     if request.method=="POST":
          program=request.POST['program']
          branch=request.POST['branch']
          year=request.POST['year']
          subject=request.POST['subject']
          link=request.POST['link']
          link_update=timezone.now()
          ab=Upload_Lecture(program=program,branch=branch,year=year,subject=subject,link=link,link_update=link_update)
          ab.save()
          messages.success(request,'Lecture Upload Successfully')
          return redirect('uplec')
     return render(request,'uploadlecture.html')

def upass(request):
     if request.method=="POST":
          program=request.POST['program']
          branch=request.POST['branch']
          year=request.POST['year']
          subject=request.POST['subject']
          new_file=request.FILES['new_file']
          file_update=timezone.now()
          ab=Upload_Asmt(program=program,branch=branch,year=year,subject=subject,new_file=new_file,file_update=file_update)
          ab.save()
          messages.success(request,'Assignments Upload Successfully')
          return redirect('upass')
     return render(request,'uploadAss.html')
def feedback(request):
     return render(request,'feedback.html')
def complaint(request):
     return render(request,'complaint.html')
def add_notification(request):
     if request.method=="POST":
          noti=request.POST['noti']
          notidate=timezone.now()
          ab=Noti(noti=noti,notidate=notidate)
          ab.save()
          messages.success(request,'Notification Added Successfully')
          return redirect('add_notification')
     return render(request,'noti.html')

     
     

        
        
        
    