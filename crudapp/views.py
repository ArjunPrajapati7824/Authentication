from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import *
from .forms import *
from django.contrib import messages

# Create your views here.





def addshow(request):
    data=User.objects.all()

    if request.method =="POST":
        form =studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('addshow'))
        else:
            return redirect(reverse_lazy('addshow'))
    else:
        form=studentform()
    return render(request,'addshow.html',{"form":form,"data":data})

def userlogin(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request, 'you are successfully logged in')
                    return redirect(reverse_lazy('profile'))
                else:
                    messages.error(request, 'Invalid userid or password')

                    return redirect(reverse_lazy(' login'))
        form=AuthenticationForm()

        return render(request,"login.html",{"form":form})
    else:
        return redirect(reverse_lazy('profile'))


def userprofile(request):
    if  request.user.is_authenticated:
        if request.method =="POST":
            form=datachange(instance=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('profile')
            else:
                return HttpResponse('something went wrong')
        form=datachange()
        return render(request,"profile.html",{"name":request.user,"form":form})
    return redirect(reverse_lazy('login'))

def changepass(request):
    if request.method=="POST":
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.error(request, 'password change successfully')
            return redirect('profile')


    else:
        fm=PasswordChangeForm(user=request.user)
    return render(request,'profile.html',{"frm":fm})


def userlogout(request):
        logout(request)
        return redirect((reverse_lazy('login')))




def updatedata(request,id):
    if request.method == "POST":
        data=User.objects.get(id=id)
        form=studentform(instance=data,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('addshow'))
        else:
            return redirect(reverse_lazy('update'))

    else:
        data=User.objects.get(id=id)

        form=studentform(instance=data)

    return render(request,'update.html',{"form":form})


def deletedata(request,id):
    data=User.objects.get(id=id)
    data.delete()
    return redirect(reverse_lazy('addshow'))
