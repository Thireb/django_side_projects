from django.forms import ModelForm, fields
from .models import Record

class RecordForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Record
        fields = [
            'Quantity', 
        ]