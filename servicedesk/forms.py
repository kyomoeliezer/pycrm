from django import forms
from .models import *
from core.models import *


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

class AttendForm(forms.ModelForm):

    ticketNo=forms.CharField(required=False)

    class Meta:
        model = CustomerQuery
        fields = [
            "status",'category','subcategory','desc','status'
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['request'].widget.attrs['class'] = 'select2'
