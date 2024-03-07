# your_app/forms.py
from django import forms
from .models import Visitor

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name', 'mobile', 'city', 'reason']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'reason': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Your Name',
            'mobile': 'Your Mobile No.',
            'city': 'Your City',
            'reason': 'Reason',
        }
