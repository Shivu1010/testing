from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import AdmissionDetail
from .models import StudentMarks


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput)



class AdmissionDetailForm(forms.ModelForm):
    class Meta:
        model = AdmissionDetail
        fields = ['name', 'email', 'phone_number']

class MarksForm(forms.ModelForm):
    class Meta:
        model = StudentMarks
        fields = ['student_name', 'roll_number', 'subject1', 'subject2', 'subject3', 'subject4', 'subject5']