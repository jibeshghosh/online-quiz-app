# pyrefly: ignore [missing-import]
from django.contrib import admin
# pyrefly: ignore [missing-import]
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.templatetags.static import static

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=static('favicon.ico'), permanent=True)),
    path('favicon.svg', RedirectView.as_view(url=static('favicon.svg'), permanent=True)),
    path('apple-touch-icon.png', RedirectView.as_view(url=static('apple-touch-icon.png'), permanent=True)),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('quizzes.urls')),
]

