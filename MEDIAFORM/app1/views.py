from django.shortcuts import render,HttpResponse
from app1.forms import movieform
from app1.models import movie

# Create your views here.

def insert(request):
    if request.method=='GET':
        var=movieform()
        return render(request,'ins.html',{'var':var})
    elif request.method=='POST' and request.FILES:
        form=movieform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('data stored in table')

def up(request,pk):
    a=movie.objects.get(id=pk)
    if request.method=='GET':
        var=movieform(instance=a)
        return render(request,'ins.html',{'var':var})
    elif request.method=='POST' or request.FILES:
        form=movieform(request.POST,request.FILES,instance=a)
        if form.is_valid():
            form.save()
            return HttpResponse('data stored in table')
def read(request):
    a=movie.objects.all()
    return render(request,'read.html',{'var':a})

def delete(request,pk):
    movie.objects.get(id=pk).delete
    return HttpResponse('record deleted')
