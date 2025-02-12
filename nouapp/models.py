from django.db import models

# Create your models here.
class tbl_login(models.Model):
 usertype=models.CharField(max_length=50)
 username=models.CharField(max_length=70)
 password=models.CharField(max_length=16)
class tbl_registration(models.Model):
    rollno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=225)
    fname=models.CharField(max_length=200)
    mname=models.CharField(max_length=225)
    gender=models.CharField(max_length=5)
    program=models.CharField(max_length=50)
    branch=models.CharField(max_length=200)
    year=models.CharField(max_length=5)
    mobile=models.CharField(max_length=14)
    email=models.CharField(max_length=200,unique=True)
    password=models.CharField(max_length=16)
    usertype=models.CharField(max_length=50)
    regdate=models.DateTimeField()
class Enquiry(models.Model):
   id=models.IntegerField(primary_key=True,auto_created=True)
   name=models.CharField(max_length=225)
   contactno=models.CharField(max_length=14)
   email=models.CharField(max_length=100)
   address=models.CharField(max_length=200)
   enqtxt=models.CharField(max_length=500)
   enqdate=models.DateTimeField()
class Upload_Study(models.Model):
   id=models.IntegerField(primary_key=True,auto_created=True)
   program=models.CharField(max_length=100)
   branch=models.CharField(max_length=200)
   year=models.CharField(max_length=5)
   subject=models.CharField(max_length=200)
   new_file=models.FileField(upload_to='Upload_study')
   file_update=models.DateField()
class Upload_Lecture(models.Model):
   id=models.IntegerField(primary_key=True,auto_created=True)
   program=models.CharField(max_length=100)
   branch=models.CharField(max_length=200)
   year=models.CharField(max_length=5)
   subject=models.CharField(max_length=200)
   link=models.CharField(max_length=200)
   link_update=models.DateField()
class Upload_Asmt(models.Model):
   id=models.IntegerField(primary_key=True,auto_created=True)
   program=models.CharField(max_length=100)
   branch=models.CharField(max_length=200)
   year=models.CharField(max_length=5)
   subject=models.CharField(max_length=200)
   new_file=models.FileField(upload_to='Upload_study')
   file_update=models.DateField()
class Noti(models.Model):
   id=models.IntegerField(primary_key=True,auto_created=True)
   noti=models.CharField(max_length=200)
   notidate=models.DateTimeField()
   



