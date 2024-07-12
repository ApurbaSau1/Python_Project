from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from.forms import MyRegForm,MyLogForm,MyContactForm,MyUserChangeFrm,MychangePwdForm
from . models import Subject,SubjectModules,SubjectDetails,CustomUser,Question,Notice
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.core.mail import send_mail 


# Create your views here.
def home(request):
    allSubject=Subject.objects.all().order_by('sub_name')
    notice=Notice.objects.all()
    context={'allSubject':allSubject,'notice':notice}
    return render(request,'main.html',context) 
   
def about(request):
    allSubject=Subject.objects.all().order_by('sub_name')
    img=Subject.objects.all()
    context={'allSubject':allSubject,'img':img}
    return render(request,'about.html',context)
 
def codding(request):
    if request.user.is_authenticated:
        allSubject=Subject.objects.all().order_by('sub_name')
        context={'allSubject':allSubject}
        return render(request,'Programming.html',context)
    else:
        return redirect('/login')
   
def contactPage(request):
    if request.POST:
        frm=MyContactForm(request.POST)
        if frm.is_valid():
            frm.save()
            msg="Your message has been send successfully"
    else:
        frm=MyContactForm()
        msg=False
    return render(request,'contact.html',{'frm':frm,'msg':msg})

def New_Registation(request):
    if request.POST:
          frm=MyRegForm(request.POST)
          if frm.is_valid():
            try:
                frm.save()
                msg="Your registration is successful"
            except Exception as e:
                return render(request,'New-Registation.html')
    else:
        frm=MyRegForm()
        msg=False
    return render(request,'New-Registation.html',{'frm':frm, 'msg':msg})



def loginPage(request):
    if request.POST:
          frm=MyLogForm(request=request, data=request.POST)
          if frm.is_valid():
              try:
                uname=frm.cleaned_data['username']
                upass=frm.cleaned_data['password']
                user=authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    # login(request,user.firstname)
                    return redirect('/')
              except Exception as e:      
                    messages.success(request,'please check your username and password')
    else:
        frm=MyLogForm()
    return render(request,'login.html',{'frm':frm})

def logoutPage(request):
    logout(request)
    return redirect('/login')

def delete(request,id):
    try:
        CustomUser.objects.filter(id=id).delete()
        messages.error(request,'Your account has been deleted')
        return redirect('/login')
    except Exception as e:
        return HttpResponse(e)


def chngeProfile(request):
    if request.user.is_authenticated:
        if request.POST:
            form = MyUserChangeFrm(request.POST, instance=request.user)
            if form.is_valid():
                if form.save():
                    messages.success(request, 'Your profile has been update successfully')
                else:
                    messages.error(request, 'Your profile has not been update successfully')
        form = MyUserChangeFrm(instance=request.user)
        context={'frm':form}
        return render(request, 'edit.html',context)
    else:
        return HttpResponseRedirect('/login')



def showCode(request):
        show=Subject.objects.all()
        return render(request,'subjectGalary.html',{'show':show})

def viewsubject_modeles(request,id):
 if request.user.is_authenticated:
    # read_code=Subject.objects.get(sub_id=id)
    sub_modules=SubjectModules.objects.filter(subject_id=id)
    show=Subject.objects.get(sub_id=id)
    # print(show)
    context={'sub_modules':sub_modules,'show':show}
    # sub_con=SubjectDetails.objects.filter()
    return render(request,'show_subject_models.html',context)
 else:
    return redirect('/login')

def viewSubject_Content(request,sub_module_id):
 if request.user.is_authenticated:
    print(sub_module_id)
    sub_read=SubjectDetails.objects.filter(sub_module_id=sub_module_id)
    return render(request,'subRead.html',{'sub_read':sub_read})
 else:
    return redirect('/login')

def userChangePassword(request):
    if request.user.is_authenticated:
        if request.POST:
            form = MychangePwdForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, request.user)
                
        else:
            form=MychangePwdForm(request.user)
        context = {'frm': form}
        return render(request, 'changpws.html', context)
    else:
        return HttpResponseRedirect('/login')
    
def examination(request):
 if request.user.is_authenticated:
    qun=Question.objects.all()
    return render(request,'exam.html',{'qun':qun})
 else:
        return redirect('/login')
