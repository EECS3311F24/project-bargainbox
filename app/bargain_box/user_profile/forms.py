from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UpdateUserTableForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class UpdateProfileTableForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    biography = forms.Textarea()

    class Meta:
        model = Profile
        fields = ['image', 'biography']
