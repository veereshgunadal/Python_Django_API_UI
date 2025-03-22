from django import forms
from app1.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'