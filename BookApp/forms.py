from django import forms
from django.contrib.auth.models import User
from .models import Reader

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")

    class Meta:
        model = Reader
        fields = ['name', 'surname', 'email', 'phone']
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'email': 'Email',
            'phone': 'Телефон',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError("Пользователь с таким Email уже зарегистрирован.")
        return email


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder': 'example@email.com'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
