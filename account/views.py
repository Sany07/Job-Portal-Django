from django.shortcuts import render, redirect
from account.forms import *
# Create your views here.


def EmployeeRegistration(request):
    """
    Handle Employee Registration

    """
    form = EmployeeRegistrationForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        return redirect('login')
    context={
        
            'form':form
        }

    return render(request,'account/employee-registration.html',context)


def EmployeeRegistration(request):
    """
    Handle Employee Registration 

    """

    form = EmployerRegistrationForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        return redirect('login')
    context={
        
            'form':form
        }

    return render(request,'account/employer-registration.html',context)



def UserLogIn(request):

    """
    Provides users to logIn

    """
    form = UserLoginForm(request.POST or None)

    if request.user.is_authenticated:
        return redirect('/')
    
    else:
        if request.method == 'POST':
            if form.is_valid():
                auth.login(request, form.get_user())
                return redirect('home')
    context = {
        'form': form,
    }

    return render(request,'account/login.html',context)


def UserLogOut(request):
    """
    Provide the ability to logout
    """
    auth.logout(request)
    messages.success(request, 'You are Successfully logged out')
    return redirect('/')