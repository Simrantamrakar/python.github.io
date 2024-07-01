from . models import Contact
from django import forms


class ContactForm(forms.Form):
    name= forms.CharField(max_length=150)
    email= forms.EmailField()
    message= forms.CharField()
    subject= forms.CharField(max_length=150)

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields ='__all__' #['name','email','conatact']