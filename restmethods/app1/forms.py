from django import forms
from app1.models import Student

class StudentForm(forms.ModelForm):
    def clean_age(self):
        input_age = self.cleaned_data['age']
        if input_age >40:
            raise forms.ValidationError('age is more')
        else:
            return input_age
    class Meta:
        model = Student
        fields = '__all__'
