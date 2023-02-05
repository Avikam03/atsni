from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate
from django.template import loader
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
import re

from .models import MyUser
from .forms import UserForm

# Create your views here.


"""
logout(request) 
    the function implements logout functionality for a user in Django.
    It uses an inbuilt function to logout the user, then redirects to the home page.
"""
def logout(request):
    django_logout(request)
    return redirect('/')

"""
register(request)
    the function implements the registration functionality for a user in Django.
    It uses a form to get the user's information, then creates a new user in the database.
    It then logs the user in and redirects to the home page.
"""
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

            if phone[3] != '-' or phone[7] != '-':
                return render(request, 'teamlist/register.html', {'form': form, 'error': 'Invalid phone number! Please use the format 123-456-7890'})

            email = form.cleaned_data['email']
            admin = form.cleaned_data['admin']

            temp = MyUser.objects.all().filter(email=email)
            print(temp)

            if len(temp) > 0:
                return render(request, 'teamlist/register.html', {'form': form, 'error': 'User with this email already exists!'})
            
            user = MyUser.objects.create_user(email, first_name, last_name, phone, admin)
            user.save()
            django_login(request, user)

            return redirect('/')
            
        else:
            print(form.errors)
            return render(request, 'teamlist/register.html', {'form': form, 'formerrors': form.errors})
    else:
        form = UserForm()
        return render(request, 'teamlist/register.html', {'form': form})

"""
login(request)
    the function implements the login functionality for a user in Django.
    It uses a form to get the user's email, then authenticates the user.
    If the user is authenticated, it logs the user in and redirects to the home page.
    If the user is not authenticated, it redirects to the login page with an error message.
"""
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

"""
index(request)
        This function is the main view for the application.
        If user is authenticated, it displays the list of users in the team.
        Else, it displays the landing page.
"""
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


"""
add(request)
    This function implements the add user (member) functionality.

    If the user is not authenticated, it redirects to the home page.
    If the user is authenticated, it displays the form to add a new user.
"""
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

            if phone[3] != '-' or phone[7] != '-':
                return render(request, 'teamlist/add.html', {'form': form, 'error': 'Invalid phone number! Please use the format 123-456-7890'})

            email = form.cleaned_data['email']
            admin = form.cleaned_data['admin']

            temp = MyUser.objects.all().filter(email=email)
            if len(temp) > 0:
                return render(request, 'teamlist/register.html', {'form': form, 'error': 'User with this email already exists!'})

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
            return render(request, 'teamlist/add.html', {'form': form, 'formerrors': form.errors})
    else:
        form = UserForm(initial={'admin': 'False'})
    return render(request, 'teamlist/add.html', {'form': form})

"""
delete(request, id)
    This function implements the delete user (member) functionality.
    It deletes the user with the given id if the current logged in user has the permissioon to do so
"""
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

"""
edit(request, id)
    This function implements the edit user (member) functionality.
    It edits the user with the given id if the current logged in user has the permissioon to do so
"""
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

            if phone[3] != '-' or phone[7] != '-':
                return render(request, 'teamlist/edit.html', {'form': form, 'error': 'Invalid phone number! Please use the format 123-456-7890'})

            email = form.cleaned_data['email']
            admin = form.cleaned_data['admin']

            if (request.user.id == user.id):
                if (('True' == admin) and (False == request.user.admin)):
                    return render(request, 'teamlist/error.html', {'error': 'You do not have permission to change your own admin status!'})
            else:
                if (request.user.admin == False):
                    return render(request, 'teamlist/error.html', {'error': 'You do not have permission to edit users as you\'re not an admin!'})

            if (user.email != email):
                if (MyUser.objects.filter(email=email).exists()):
                    return render(request, 'teamlist/edit.html', {'form': form, 'error': 'Email already exists!'})

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
            return render(request, 'teamlist/edit.html', {'form': form, 'formerrors': form.errors})
            
    else:
        form = UserForm({ 'first_name': user.first_name, 'last_name': user.last_name, 'phone': user.phone, 'email': user.email, 'admin': user.admin})
    return render(request, 'teamlist/edit.html', {'user': user, 'form': form})