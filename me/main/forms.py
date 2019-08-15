from django import forms

class SignUp(forms.Form):
    email = forms.CharField(label="Email", max_length=400)