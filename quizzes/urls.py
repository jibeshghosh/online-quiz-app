# pyrefly: ignore [missing-import]
from django.urls import path
# pyrefly: ignore [missing-import]
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('quizzes/', views.quiz_list, name='quiz_list'),
    path('quizzes/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quizzes/<int:quiz_id>/attempt/', views.quiz_attempt, name='quiz_attempt'),
    path('quizzes/<int:attempt_id>/submit/', views.quiz_submit, name='quiz_submit'),
    path('quizzes/attempt/<int:attempt_id>/result/', views.quiz_result, name='quiz_result'),
    path('quizzes/attempt/<int:attempt_id>/review/', views.quiz_review, name='quiz_review'),
    path('my-results/', views.my_results, name='my_results'),
    path('profile/', views.profile, name='profile'),
    

    # Password Reset OTP URLs
    path('password-reset/', views.password_reset_request, name='password_reset'),
    path('password-reset/verify/', views.password_reset_verify, name='password_reset_verify'),

]

