from django import forms

class UserForm(forms.Form):
    template_name = "teamlist/user.html"

    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    phone = forms.CharField(max_length=12)
    email = forms.EmailField()

    CHOICES = [
        ('True', 'Admin - Can delete members'),
        ('False', 'Regular - Can\'t delete members'),
    ]
    admin = forms.ChoiceField(
        label='Role',
        widget=forms.RadioSelect,
        choices=CHOICES, 
    )

