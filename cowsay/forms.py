from django import forms
from cowsay.models import UserInput

class CowsayAddForm(forms.Form):
    user_input = forms.CharField(widget=forms.Textarea)