from django import forms
from .models import Message
from django.core.validators import ValidationError


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=10, label='your name')
    text = forms.CharField(max_length=10, label='your message')

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise ValidationError('name and text are same', code='name_text_same')


class MessageForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your message'}))
    age = forms.IntegerField()
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))


