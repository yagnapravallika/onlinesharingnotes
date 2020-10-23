from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Student,Teacher,Fileupload
from .forms import Studentform,Teacherform,Fileuploadeform

# Create your views here.
def mainpage(request):
    return render(request,"main.html")


def teacherlogin(request):
    tname=request.POST['a']
    tpassword=request.POST['b']

    k=Teacher.objects.get(name=tname,password=tpassword)
    request.session['name']=k.name

    t=Fileuploadeform()
    return render(request,"fileuploade.html",{"form":t})

def filesave(request):
    if request.POST:
        request.session['name']
        form = Fileuploadeform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,"fileuploade.html",{"message":"data saved"})
def tlogout(request):
    del request.session['name']
    return redirect('main')

def teacherregister(request):
    return render(request,"teacherregister.html",{"form":Teacherform()})

def teacherregistersaved(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    password = request.POST.get("password")
    subject= request.POST.get("subject")
    classno=request.POST.get("classno")
    Teacher(idno=idno,name=name,password=password,subject=subject,classno=classno).save()
    return redirect('main')
def studentlogin(request):
    sname = request.POST['a']
    spasword = request.POST['b']
    sclass= request.POST['c']
    s=Student.objects.get(name=sname, password=spasword,classno=sclass)
    request.session['name'] = s.name
    k=Fileupload.objects.filter(classno=sclass)
    return render(request, "viewstudent.html",{"student":k})

def studentregister(request):
    return render(request,'studentregister.html',{"form":Studentform()})

def studentregistersaved(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    password = request.POST.get("password")
    classno = request.POST.get("classno")
    Student(idno=idno, name=name, password=password, classno=classno).save()
    return redirect('main')


def slogout(request):
    return redirect('main')


# def wholenotes(request):
#     q1=Fileupload.objects.filter()
#     return render(request,'wholenotes.html',{'wholenotes':})