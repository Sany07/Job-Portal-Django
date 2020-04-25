from django.shortcuts import render, redirect
from account.forms import *
# Create your views here.


def EmployeeRegistration(request):

    form = EmployeeRegistrationForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        return redirect('/')
    context={
        
            'form':form
        }

    return render(request,'account.html',context)



def UserLogIn(request):


    form = UserLoginForm(request.POST or None)

    if request.user.is_authenticated:
        return redirect('/')
    
    else:
        if request.method == 'POST':
            if form.is_valid():
                auth.login(request, form.get_user())
                return redirect('home')
    context = {
        'lform': form,
    }

    return render(request,'account.html',context)

