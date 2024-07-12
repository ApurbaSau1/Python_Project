from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html
from django.utils.html import mark_safe

# Create your models here.

class CustomUser(AbstractUser):
      contact_no=models.CharField(max_length=12)
      gender=models.CharField(max_length=10)
      
      
class Subject(models.Model):     #table 1
  sub_id=models.AutoField(primary_key=True)
  sub_name=models.CharField(max_length=255,unique='True',verbose_name='Subject Name')
  sub_img = models.FileField(upload_to='upload/',verbose_name='Subject Image')
  def subject_Img(self): #new
        return mark_safe(f'<img src = "{self.sub_img.url}" width = "30" height ="30" />')  


class SubjectModules(models.Model):        #table 2
  sub_module_id=models.AutoField(primary_key=True)
  module_name=models.CharField(max_length=255)
  module_desc=models.TextField()
  subject=models.ForeignKey(Subject,on_delete=models.CASCADE,verbose_name='Subject')    #foreignKey
# @property
# def id(args):
    
 
class SubjectDetails(models.Model):        #table 3
  sub_det_id=models.AutoField(primary_key=True)
  sub_module=models.ForeignKey(SubjectModules,on_delete=models.CASCADE,verbose_name='Subject Modules')  #foreignKey
  subject=models.ForeignKey(Subject,on_delete=models.CASCADE,verbose_name='Subject') #foreignKey
  sub_cont=models.TextField(verbose_name='Subject Content') 
    
  # @property
  # def id(self):
  #  return self.sub_module.sub_module
  
class Contact(models.Model):
    name = models.CharField(max_length=150,verbose_name='Contact Name')
    email = models.CharField(max_length=255,verbose_name='Email Address')
    msg = models.TextField(verbose_name='Message')
    date = models.DateField(auto_now_add=True,blank=False)

class Notice(models.Model):
   notice=models.CharField(max_length=500)
    
  
class Question(models.Model):
  question=models.CharField( max_length=250)
  op1=models.CharField(max_length=250)
  op2=models.CharField(max_length=250)
  op3=models.CharField(max_length=250)
  op4=models.CharField(max_length=250)
  ans=models.CharField(max_length=250)
  sub=models.ForeignKey(Subject,models.CASCADE,verbose_name='Subject Name')
  

