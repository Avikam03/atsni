from django import forms

class AddMemberForm(forms.Form):
    template_name = "teamlist/member.html"

    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    phone = forms.CharField(max_length=12)
    email = forms.EmailField()
    admin = forms.BooleanField(required=False)

class EditMemberForm(forms.Form):
    template_name = "teamlist/member.html"
    
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    phone = forms.CharField(max_length=12)
    email = forms.EmailField()
    admin = forms.BooleanField(required=False)