from .models import signup,login
from django import forms

class signupForm(forms.ModelForm):
    class Meta():
        model = signup
        fields = '__all__'

class loginForm(forms.ModelForm):
    class Meta():
        model = login
        fields = "__all__"
        