from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-input', 'placeholder': 'Enter your first name'
    }))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-input', 'placeholder': 'Enter your last name'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-input', 'placeholder': 'Enter your email'
    }))

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'class': 'form-input textarea-input', 'rows': 4, 'placeholder': 'Tell us a bit about yourself...'
    }))

    class Meta:
        model = UserProfile
        fields = ['bio']


from django.contrib.auth.forms import PasswordResetForm
from django.db.models import Q

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Enter registered email or username',
            'autofocus': True
        })
    )

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip()
        users = list(self.get_users(email))
        if not users:
            raise forms.ValidationError("No registered active user account was found with that email address or username.")
        return email

    def get_users(self, email):
        """
        Given an email or username, return matching active users.
        Removes unusable password restriction so all active users can reset/set their password.
        """
        email = email.strip()
        active_users = User.objects.filter(
            Q(email__iexact=email) | Q(username__iexact=email),
            is_active=True
        )
        return list(active_users)

