# pyrefly: ignore [missing-import]
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
# pyrefly: ignore [missing-import]
from django.contrib.auth.models import User
import re

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    """
    Custom adapter for handling django-allauth social login & auto signup seamlessly.
    Automatically connects incoming social accounts to existing local users with matching email addresses,
    and guarantees unique username generation for new social accounts.
    """

    def pre_social_login(self, request, sociallogin):
        # 1. If already linked to an existing User object, nothing to do
        if sociallogin.is_existing:
            return

        # 2. Extract email from social account details
        email = None
        if sociallogin.user and sociallogin.user.email:
            email = sociallogin.user.email
        elif sociallogin.email_addresses:
            for email_obj in sociallogin.email_addresses:
                if email_obj.email:
                    email = email_obj.email
                    break

        if not email:
            return

        # 3. Check if user with matching email already exists in Django DB
        try:
            user = User.objects.get(email__iexact=email)
            # Connect the social login to existing user
            sociallogin.connect(request, user)
        except User.DoesNotExist:
            pass

    def is_auto_signup_allowed(self, request, sociallogin):
        """Always allow auto signup without interrupting the user flow."""
        return True

    def populate_user(self, request, sociallogin, data):
        """Populate user fields and ensure username is 100% unique."""
        user = super().populate_user(request, sociallogin, data)
        
        # Ensure email is populated
        if not user.email and data.get('email'):
            user.email = data.get('email')

        # Ensure first_name and last_name are populated from extra_data if available
        extra_data = sociallogin.account.extra_data or {}
        if not user.first_name:
            user.first_name = extra_data.get('given_name') or extra_data.get('first_name') or ''
        if not user.last_name:
            user.last_name = extra_data.get('family_name') or extra_data.get('last_name') or ''

        # Generate a clean, unique username if missing or already taken
        base_username = user.username
        if not base_username and user.email:
            base_username = user.email.split('@')[0]
        if not base_username:
            base_username = f"user_{sociallogin.account.provider}"

        # Clean username to allowed characters: alphanumeric and underscores/hyphens/dots
        base_username = re.sub(r'[^\w.-]', '_', base_username)
        
        username = base_username
        counter = 1
        # Loop until unique username is found
        while User.objects.filter(username__iexact=username).exists():
            username = f"{base_username}_{counter}"
            counter += 1
            
        user.username = username
        return user
