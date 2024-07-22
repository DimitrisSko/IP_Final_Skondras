
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

class CustomUserChangeForm(UserChangeForm):

    # Custom form for editing user details and password.

    # Inherits from UserChangeForm and adds a custom password field.
    
    password = forms.CharField(
        widget=forms.PasswordInput,  # Renders the field as a password input (masked characters)
        help_text="Leave empty if not changing."  # Help text for the password field
    )

    class Meta:
        model = User  # Specifies the model associated with this form
        fields = ('username', 'first_name', 'last_name', 'password')  # Fields to include in the form