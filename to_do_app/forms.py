from django import forms

class ToDO(forms.Form):
    todo = forms.CharField(max_length=100)
    