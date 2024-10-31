from django.contrib.auth.forms import BaseUserCreationForm
from django import forms
from authentication.models import User


class RegistrationForm(BaseUserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = "Email Address"
