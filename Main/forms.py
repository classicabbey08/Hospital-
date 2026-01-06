from django import forms
from .models import Contact
from .models import Contact


class  Contactform(forms.ModelForm):
    class Meta:
        model= Contact
        fields= ['name', 'email', 'subject', 'phone', 'message']

        from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "subject", "message"]
