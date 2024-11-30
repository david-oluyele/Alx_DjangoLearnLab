#Form to handle input validation for user data

from django import forms

class ExampleForm(forms.Form):
    query = forms.CharField(max_length=100, required=True)

