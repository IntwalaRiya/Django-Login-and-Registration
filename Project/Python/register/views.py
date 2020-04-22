from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RegisterForm, LoginForm
from .models import Submit

#Registration View
def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'Register.html'
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                user = Submit.objects.create(Username = form.cleaned_data['username'],Mail = form.cleaned_data['email'],Password = form.cleaned_data['password'],
                Phone =form.cleaned_data['phone_number'],FirstName = form.cleaned_data['first_name'],LastName = form.cleaned_data['last_name'])
                user.save()
               
                # redirect to accounts page:
                return HttpResponseRedirect('/Register')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()
        return render(request, template, {'form': form})
    
    # form = RegisterForm()
    # return render(request, template, {'form': form})
    return HttpResponseRedirect('/Register')

#Login View
def user_login(request):
    # if this is a POST request we need to process the form data
    template = 'Login.html'
    if(request.method == 'POST'):
        mail = request.POST.get('email')
        password =request.POST.get('password')
        if((Submit.objects.filter(Mail = mail).exists()) and (Submit.objects.filter(Password = password ).exists())):
            return HttpResponseRedirect('/Page')
        else:
            return HttpResponseRedirect('/Login')
    else:
        form = LoginForm()
        return render(request, template, {'form': form})
    
    form = LoginForm()
    return render(request, template, {'form': form})

#Home View
def user_home(request):
    return render(request,'Page.html')