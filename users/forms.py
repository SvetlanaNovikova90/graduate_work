from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User, Recording


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class VerificationCodeForm(forms.Form):
    verification_code = forms.CharField(max_length=8, label='Код верификации')


class RecordingForm(forms.ModelForm):
    class Meta:
        model = Recording
        fields = ('doctor', 'service', 'datetime_rec')
