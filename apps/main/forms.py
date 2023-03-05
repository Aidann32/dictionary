from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class KazakhAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Логин',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label='Құпия сөз',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
        

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Пошта')
    password1 = forms.CharField(
        label='Құпия сөз',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='Құпия сөзіңізде кемінде 8 таңба болуы керек.',
    )
    password2 = forms.CharField(
        label='Құпия сөзді растау',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text='Тексеру үшін үстіндегідей құпия сөзді енгізіңіз.',
    )
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        labels = {
            'username':'Логин'
            }
        help_texts = {
            'username': 'Қажетті. 150 таңба немесе одан аз. Тек әріптер, сандар және @/./+/-/_.'
        }
    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user