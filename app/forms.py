from django import forms

class Stringform(forms.Form):
    string = forms.CharField(max_length=500)

class nhform(forms.Form):
    number = forms.IntegerField()

class lsform(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()

class cd_form(forms.Form):
    string = forms.CharField(max_length=200)