from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "mobile", "location"]



class SeachData(forms.ModelForm):
    seach_name = forms.CharField(label='Search Name/', required=False)
    fromdate=forms.DateField(label='From Date',required=False,widget=forms.widgets.DateInput(
        attrs={'type': 'date'}))
    todate = forms.DateField(label='To Date', required=False,widget=forms.widgets.DateInput(
        attrs={'type': 'date'}))
    mobile=forms.CharField(required=False)

    class Meta:
        model=Contact
        fields=('mobile',)

