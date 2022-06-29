from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Website Name", max_length=100)
    desc = forms.CharField(label="Website Name", max_length=10000)
    ToS = forms.BooleanField(label="Agree to ToS")