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


from django.db.models import Q

class RequestOTPForm(forms.Form):
    email_or_username = forms.CharField(
        max_length=254,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Enter registered email or username',
            'autofocus': True,
            'autocomplete': 'off'
        })
    )

    def clean_email_or_username(self):
        val = self.cleaned_data.get('email_or_username', '').strip()
        users = User.objects.filter(
            Q(email__iexact=val) | Q(username__iexact=val),
            is_active=True
        )
        if not users.exists():
            raise forms.ValidationError("No active user account was found with that email address or username.")
        return val


class VerifyOTPResetForm(forms.Form):
    otp = forms.CharField(
        max_length=6,
        min_length=6,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Enter 6-digit OTP code',
            'style': 'letter-spacing: 6px; font-size: 1.3rem; font-weight: 700; text-align: center;',
            'maxlength': '6',
            'autofocus': True,
            'autocomplete': 'off'
        })
    )
    new_password = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Choose new password'
        })
    )
    confirm_password = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Confirm new password'
        })
    )

    def clean_otp(self):
        otp = self.cleaned_data.get('otp', '').strip()
        if not otp.isdigit():
            raise forms.ValidationError("OTP code must contain digits only.")
        return otp

    def clean(self):
        cleaned_data = super().clean()
        pw = cleaned_data.get('new_password')
        confirm_pw = cleaned_data.get('confirm_password')

        if pw and confirm_pw:
            if pw != confirm_pw:
                self.add_error('confirm_password', "Passwords do not match.")
            elif len(pw) < 8:
                self.add_error('new_password', "Password must be at least 8 characters long.")
        return cleaned_data



