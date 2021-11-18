from django import forms
from django.forms import widgets
from .models import Contact, SendEmail , Comment
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']

# class LoginForm(forms.ModelForm):
#     password = forms.CharField(
#         label='Password',
#         widget=forms.PasswordInput(attrs={'class':'form-control'})
#     )

#     def init(self, *args, **kwargs):
#         super().init(*args, **kwargs)
#         self.fields['username'].label = 'Username'
#         self.fields['password'].label = 'Password'
#     def clean(self):
#         username = self.cleaned_data['username']
#         password = self.cleaned_data['password']
#         if not User.objects.filter(username=username).exists():
#             raise forms.ValidationError(f'The user {username} is not defined.')
#         user = User.objects.filter(username=username).first()
#         if user:
#             if not user.check_password(password):
#                 raise forms.ValidationError('Password is not correct')
#             return self.cleaned_data
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         widgets = {
#             'username' : forms.TextInput(attrs={'class':'form-control'}),
#         }