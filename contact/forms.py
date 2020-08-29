from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
	contact_name = forms.CharField(required=True, widget=forms.TextInput(), label='name')
	contact_email = forms.EmailField(required=True, widget=forms.TextInput(),label='email')
	content = forms.CharField(required=True, widget=forms.Textarea(), label='message')
