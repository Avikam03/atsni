from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader

from .models import Member
from .forms import MemberForm


# Create your views here.
def index(request):
    member_list = Member.objects.all()
    context = {
        'member_list': member_list,
        'length' : len(member_list),
    }
    return render(request, 'teamlist/index.html', context)


def add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MemberForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            admin = form.cleaned_data['admin']

            member = Member(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                admin=admin
            )

            member.save()
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = MemberForm(initial={'admin': 'False'})
    return render(request, 'teamlist/add.html', {'form': form})

def delete(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST' and member:
        member.delete()
        return redirect('/')

def edit(request, id):
    member = get_object_or_404(Member, id=id)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MemberForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            admin = form.cleaned_data['admin']

            member.first_name = first_name
            member.last_name = last_name
            member.phone = phone
            member.email = email
            member.admin = admin

            member.save()
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = MemberForm({ 'first_name': member.first_name, 'last_name': member.last_name, 'phone': member.phone, 'email': member.email, 'admin': member.admin})
    return render(request, 'teamlist/edit.html', {'member': member, 'form': form})