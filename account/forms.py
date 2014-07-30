#-*- coding: utf-8 -*-
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from .models import Account

class AccountCreateForm(forms.ModelForm):
    """error_messages = {
      'duplicate_email': "A user with that e-mail already exists.",
      'email_mismatch': "The two e-mail fields didn't match.",
      'password_mismatch': "비밀번호가 같지 않습니다.",
    }"""

    username = forms.EmailField(widget=forms.widgets.EmailInput(attrs={'placeholder': 'Your email', 'class':'sign-in-input form_row'}))
    password1 = forms.CharField(min_length=3, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password', 'class':'sign-in-input form_row'}))
    password2 = forms.CharField(min_length=3, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password confirm', 'class':'sign-in-input form_row'}))
 
    def is_valid(self):
        form = super(AccountCreateForm, self).is_valid()

        return form
 
    class Meta:
        model  = Account
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username == 'customform':
            raise forms.ValidationError('custom form error')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        print "!1111111111111111111"
        user = super(AccountCreateForm, self).save(commit=False)
        print user

        print dir(user)
        print type(user)

        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class AccountAuthForm(AuthenticationForm):
    """error_messages = {
        'duplicate_email': "A user with that e-mail already exists.",
        'email_mismatch': "The two e-mail fields didn't match.",
        'invalid_login': "이메일이나 비밀번호가 정확하지 않습니다.",
    }"""

    username = forms.EmailField(widget=forms.widgets.EmailInput(attrs={'placeholder': 'Email', 'class':'sign-in-input form_row'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password', 'class':'sign-in-input form_row'}))
 
    def is_valid(self):
        form = super(AccountAuthForm, self).is_valid()

        return form


