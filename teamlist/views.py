from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate
from django.template import loader
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
import re

from .models import MyUser
from .forms import UserForm



# Create your views here.

def logout(request):
    django_logout(request)
    return redirect('/')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
        
    if request.method == 'POST':
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']

            phone_regex = '^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'
            if not re.match(phone_regex, phone):
                return render(request, 'teamlist/register.html', {'form': form, 'error': 'Invalid phone number!'})

            email = form.cleaned_data['email']
            admin = form.cleaned_data['admin']

            user = MyUser.objects.create_user(email, first_name, last_name, phone, admin)

            user.save()
            django_login(request, user)

            return redirect('/')
        else:
            print(form.errors)
    else:
        form = UserForm()
        return render(request, 'teamlist/register.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        print("Hello")
        email = request.POST['email']
        user = authenticate(email)
        print("Hello2")

        if user is not None:
            print("authenticated here!")
            django_login(request, user)
            print("logged in!")
            return redirect('/')
        else:
            return render(request, 'teamlist/login.html', {'error': 'There is no account with this email!'})
    
    return render(request, 'teamlist/login.html', {})


def index(request):
    if request.user.is_authenticated:
        user_list = MyUser.objects.all()
        context = {
            'user_list': user_list,
            'length' : len(user_list),
        }
        return render(request, 'teamlist/index.html', context)
    else:
        return render(request, 'teamlist/landing.html', {})


def add(request):
    if not request.user.is_authenticated:
        return redirect('/')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']

            phone_regex = '^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'
            if not re.match(phone_regex, phone):
                return render(request, 'teamlist/add.html', {'form': form, 'error': 'Invalid phone number!'})

            email = form.cleaned_data['email']
            admin = form.cleaned_data['admin']

            user = MyUser(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                admin=admin
            )

            user.save()
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = UserForm(initial={'admin': 'False'})
    return render(request, 'teamlist/add.html', {'form': form})

def delete(request, id):
    if not request.user.is_authenticated:
        return redirect('/')

    user = get_object_or_404(MyUser, id=id)
    if request.method == 'POST' and user:
        if (request.user.admin == True):
            if (request.user.id == user.id):
                return render(request, 'teamlist/error.html', {'error': 'You cannot delete yourself!'})
            else:
                user.delete()
                return redirect('/')
        else:
            return render(request, 'teamlist/error.html', {'error': 'You do not have permission to delete users as you\'re not an admin!'})

def edit(request, id):
    if not request.user.is_authenticated:
        return redirect('/')

    user = get_object_or_404(MyUser, id=id)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            # process the data in form.cleaned_data as required
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']

            phone_regex = '^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'
            if not re.match(phone_regex, phone):
                return render(request, 'teamlist/edit.html', {'form': form, 'error': 'Invalid phone number!'})

            email = form.cleaned_data['email']
            admin = form.cleaned_data['admin']

            if (request.user.id == user.id):
                if (('True' == admin) and (False == request.user.admin)):
                    return render(request, 'teamlist/error.html', {'error': 'You do not have permission to change your own admin status!'})
            else:
                if (request.user.admin == False):
                    return render(request, 'teamlist/error.html', {'error': 'You do not have permission to edit users as you\'re not an admin!'})

            user.first_name = first_name
            user.last_name = last_name
            user.phone = phone
            user.email = email
            if (admin == 'True'):
                user.admin = True
            else:
                user.admin = False

            user.save()
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = UserForm({ 'first_name': user.first_name, 'last_name': user.last_name, 'phone': user.phone, 'email': user.email, 'admin': user.admin})
    return render(request, 'teamlist/edit.html', {'user': user, 'form': form})