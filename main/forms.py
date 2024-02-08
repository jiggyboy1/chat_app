from django import forms
from .models import Room


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