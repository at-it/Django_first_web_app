from django import forms
from .models import Participant


"""
# More convenient way of defining the form

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['email']
"""

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your email')