from django.urls import path
from .views import SignUpView, edit_profile

urlpatterns = [
    # URL pattern for user signup
    path('accounts/', SignUpView.as_view(), name='signup'),

    # URL pattern for editing user profile
    path('edit_profile/', edit_profile, name='edit_profile'),
]
