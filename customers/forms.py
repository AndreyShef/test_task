from django import forms


class RegForm(forms.Form):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))