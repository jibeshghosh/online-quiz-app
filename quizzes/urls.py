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
    

    # Password Reset URLs
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='quizzes/password_reset_form.html',
        email_template_name='quizzes/password_reset_email.html',
        subject_template_name='quizzes/password_reset_subject.txt'
    ), name='password_reset'),
    
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='quizzes/password_reset_done.html'
    ), name='password_reset_done'),
    
    path('password-reset-confirm/<str:uidb64>/<str:token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='quizzes/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='quizzes/password_reset_complete.html'
    ), name='password_reset_complete'),
]

