from django import forms
from .models import Course

class CreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'price', 'author']

