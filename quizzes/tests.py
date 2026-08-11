from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from decimal import Decimal
from quizzes.models import Quiz, Question, QuizAttempt

class QuizAppTests(TestCase):
    def setUp(self):
        # Create standard test user
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpassword123', 
            first_name='Test', 
            last_name='User',
            email='test@example.com'
        )
        self.client = Client()

        # Create standard test quiz
        self.quiz = Quiz.objects.create(
            title='Test Quiz',
            description='This is a description',
            category='Programming',
            difficulty='Easy',
            time_limit=10,
            pass_mark=60,
            is_published=True
        )

        # Create standard test question
        self.question = Question.objects.create(
            quiz=self.quiz,
            question_text='What is 2+2?',
            option_a='3',
            option_b='4',
            option_c='5',
            option_d='6',
            correct_option='B',
            explanation='2+2 equals 4'
        )

    def test_landing_page(self):
        """Verify the public landing page loads successfully."""
        response = self.client.get(reverse('landing'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Quiznapse")

    def test_login_page(self):
        """Verify login page loads successfully."""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        """Verify registration page loads successfully."""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_register_user_post(self):
        """Verify submitting registration form creates user and logs in without 500 error."""
        response = self.client.post(reverse('register'), {
            'username': 'newuser123',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'newuser123@example.com',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!'
        })
        self.assertRedirects(response, reverse('dashboard'))
        self.assertTrue(User.objects.filter(username='newuser123').exists())

    def test_quiz_attempt_requires_login(self):
        """Verify that starting a quiz requires authentication."""
        response = self.client.get(reverse('quiz_attempt', args=[self.quiz.id]))
        self.assertNotEqual(response.status_code, 200)  # Redirects to login

    def test_profile_statistics(self):
        """Verify calculations of attempts, average score, and pass rates on the user profile."""
        profile = self.user.profile
        self.assertEqual(profile.total_attempts_count, 0)
        self.assertEqual(profile.average_score, 0.0)

        # Simulate a passed attempt
        from django.utils import timezone
        timezone_now = timezone.now()
        QuizAttempt.objects.create(
            user=self.user,
            quiz=self.quiz,
            score=1,
            percentage=Decimal('100.0'),
            completed_at=timezone_now,
            time_taken=60,
            status='Passed'
        )

        self.assertEqual(profile.total_attempts_count, 1)
        self.assertEqual(profile.average_score, 100.0)
        self.assertEqual(profile.pass_rate, 100.0)



    def test_social_auth_google_url(self):
        """Verify Google login provider renders chooser page successfully."""
        response = self.client.get(reverse('google_login_mock'))
        self.assertEqual(response.status_code, 200)

    def test_social_auth_github_url(self):
        """Verify GitHub login provider renders chooser page successfully."""
        response = self.client.get(reverse('github_login_mock'))
        self.assertEqual(response.status_code, 200)

    def test_custom_social_account_adapter_pre_social_login(self):
        """Verify CustomSocialAccountAdapter connects existing user account by email."""
        from quizzes.adapters import CustomSocialAccountAdapter
        from unittest.mock import MagicMock

        adapter = CustomSocialAccountAdapter()
        request = MagicMock()
        sociallogin = MagicMock()
        sociallogin.is_existing = False
        sociallogin.user.email = 'test@example.com'
        sociallogin.email_addresses = []

        adapter.pre_social_login(request, sociallogin)
        sociallogin.connect.assert_called_once_with(request, self.user)

    def test_custom_social_account_adapter_populate_user_unique_username(self):
        """Verify CustomSocialAccountAdapter generates unique usernames when base username exists."""
        from quizzes.adapters import CustomSocialAccountAdapter
        from unittest.mock import MagicMock

        adapter = CustomSocialAccountAdapter()
        request = MagicMock()
        sociallogin = MagicMock()
        sociallogin.account.provider = 'google'
        sociallogin.account.extra_data = {'given_name': 'Test', 'family_name': 'User'}

        # Try populating a user whose username would be 'testuser' (which exists in setUp)
        fake_user = User(email='testuser@gmail.com', username='testuser')
        populated_user = adapter.populate_user(request, sociallogin, {'email': 'testuser@gmail.com'})
        
        self.assertNotEqual(populated_user.username, 'testuser')
        self.assertTrue(populated_user.username.startswith('testuser_'))




