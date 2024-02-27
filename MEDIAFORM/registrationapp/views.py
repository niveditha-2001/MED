from django.shortcuts import render,HttpResponse
from registrationapp.models import registration
from registrationapp.forms import rgform
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.core.mail import send_mail


def reg(request):
    if request.method=='GET':
        var=rgform()
        return render(request,'rg.html',{'var':var})
    elif request.method=='POST':
        form=rgform(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            p=form.password
            enc=make_password(p)
            form.password=enc
            #using above four lines the data will be secure otherwise hackers will hack easily
            form.save()
            subject = 'not come to pyspiders'
            message = f'Hi {form.username}, thank you for registering and your username :{form.username} password:{p}'
            email_form = settings.EMAIL_HOST_USER
            recipient_list = [form.email]
            send_mail(subject, message, email_form, recipient_list)
            return HttpResponse('data stored in a table and sent mail')
        
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
def login(request):
    if request.method=='GET':
        var=AuthenticationForm()
        return render(request,'login.html',{'var':var})
    elif request.method=='POST':
        user=request.POST['username']
        pas=request.POST['password']
        v=authenticate(username=user,password=pas)
        if v is not None:
            return render(request,'home.html')
        else:
            return HttpResponse('check username or password')
        

