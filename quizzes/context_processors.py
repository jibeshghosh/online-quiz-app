import os

def social_auth_status(request):
    """Exposes provider configuration statuses to templates to handle missing client IDs elegantly."""
    return {
        'GOOGLE_AUTH_CONFIGURED': bool(os.environ.get('GOOGLE_CLIENT_ID')),
        'GITHUB_AUTH_CONFIGURED': bool(os.environ.get('GITHUB_CLIENT_ID')),
        'EMAIL_SMTP_CONFIGURED': bool(os.environ.get('EMAIL_HOST_USER', '').strip() and os.environ.get('EMAIL_HOST_PASSWORD', '').strip()),
        'EMAIL_HOST_USER_SET': os.environ.get('EMAIL_HOST_USER', '').strip(),
    }

