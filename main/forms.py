from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Website Name", max_length=200)
    ToS = forms.BooleanField(label="Agree to ToS")