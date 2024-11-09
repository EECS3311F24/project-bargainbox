from django import forms
from django.contrib.auth.models import User

class UpdateUserProfileForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
