from django import forms
from .models import userinputs

class UserInputForm(forms.ModelForm):
    class Meta:
        model = userinputs
        fields = ['m_name', 'u_name', 'review', 'rating']
