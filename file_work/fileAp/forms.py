from django.forms import ModelForm
from django import forms
from .models import QuoteModel


class QuoteForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = QuoteModel
        fields = '__all__'
