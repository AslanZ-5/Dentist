from django import forms

from .models import Profile,User





class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class UserProfileForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields= ['username','email']
