from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(required=True, )
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField()


class ForgetForm(forms.Form):
    user_acc = forms.EmailField(required=True)
    captcha = CaptchaField()


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)
