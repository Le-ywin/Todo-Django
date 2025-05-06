from django import forms
from .models import User,TaskModel


class UserregistrationForm(forms.ModelForm):

    class Meta:

        model = User

        fields = ['username','password','email']

        widgets = {
            "username": forms.TextInput(attrs={"class":"form-control w-50 mx-auto my-2","placeholder":"Enter your username"}),
            "password": forms.PasswordInput(attrs={"class":"form-control w-50 mx-auto my-2","placeholder":"Password"}),
            "email": forms.EmailInput(attrs={"class":"form-control w-50 mx-auto my-2","placeholder":"Your email"}),
            
        }

        help_texts = {
            'username': None
    }
        
class LoginForm(forms.Form):

    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control w-50 mx-auto my-2","placeholder":"Enter your username"}))

    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control w-50 mx-auto my-2","placeholder":"Password"}))
    
class TaskForm(forms.ModelForm):

    class Meta:

        model = TaskModel

        exclude = ['created_date','user_id','completed_status']


class ForgotPasswordForm(forms.Form):

    email = forms.CharField(max_length=100)



class OtpForm(forms.Form):

    otp = forms.CharField(max_length=4)



class PwdResetForm(forms.Form):

    password = forms.CharField(max_length=50)

    confirm_password = forms.CharField(max_length=50)