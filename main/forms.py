from typing import Any
from django import forms
from .models import Room,Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateRoom(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name','topic','description']
        exclude = ['host']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a name'}),
            'topic': forms.Select(attrs={'class':'form-select','placeholder':'Enter a Topic'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter a Topic'}),
        }

class Registeruser(UserCreationForm):
    email = forms.EmailField(max_length=30,widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(Registeruser,self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
        

class UserProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','zip_code','address','photo']
        exclude = ['user']
    
        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Your Bio'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Zip code'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Address'}),
        }
