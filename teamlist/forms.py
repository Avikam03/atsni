from django import forms

class UserForm(forms.Form):
    template_name = "teamlist/user.html"

    first_name = forms.CharField(label='First Name', max_length=30, widget=forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 '}))
    last_name = forms.CharField(label='Last Name', max_length=30, widget=forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 '}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 '}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 '}))

    CHOICES = [
        ('True', 'Admin - Can delete members'),
        ('False', 'Regular - Can\'t delete members'),
    ]
    admin = forms.ChoiceField(
        label='Role',
        widget=forms.RadioSelect,
        choices=CHOICES, 
    )

