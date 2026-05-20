from django import forms
from .models import User
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length= 50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    role = forms.ChoiceField(
        choices= [
            ('admin', 'Admin'),
            ('teacher', 'Teacher'),
            ('student', 'Student'),
            ]
        )
    
    # USERNAME VALIDATION
    def clear_username(self):
        username = self.cleaned_data['username']

        if len(username) < 10:

            raise forms.ValidationError(
                "Username Must Be At Least 5 Chaaracters"
            )
        if not username.isalnum():

            raise forms.ValidationError(
                "Username Must Contain Only Letters And Numbers"
            )
        return username
    
    # EMAIL VALIDATION
    def clean_email(self):

        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():

            raise forms.ValidationError(
                "Email  Already Exists"
            )
        return email
    
    # PASSWORD VALIDATION
    def clean_password(self):

        password = self.cleaned_data['password']

        if len(password) < 6:

            raise forms.ValidationError(
                "Password Cannot Be Only Numbers"
            )
        return password
