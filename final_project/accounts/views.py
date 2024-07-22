from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserChangeForm, PasswordChangeForm

@login_required
def edit_profile(request):

    # View to handle user profile editing and password changes.

    # Requires the user to be logged in. Handles both profile updates and password changes.

    if request.method == 'POST':
        # Handle form submissions for both user profile update and password change
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)

        if user_form.is_valid() and password_form.is_valid():
            # Save profile changes
            user_form.save()
            user = password_form.save()
            # Update session hash to keep the user logged in after password change
            update_session_auth_hash(request, user)
            # Redirect to the same page to avoid resubmission of the form
            return redirect('edit_profile')
    else:
        # Initialize forms with current user data
        user_form = CustomUserChangeForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)
    
    # Render the profile edit form template
    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'password_form': password_form
    })

class SignUpView(generic.CreateView):
    # View to handle user registration.

    # Uses Django's built-in UserCreationForm for user registration.

    form_class    = UserCreationForm
    success_url   = reverse_lazy('login')  # Redirect to login page upon successful registration
    template_name = 'signup.html'  # Template for the signup form
