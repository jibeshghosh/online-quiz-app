# pyrefly: ignore [missing-import]
from django.db import models
# pyrefly: ignore [missing-import]
from django.contrib.auth.models import User
# pyrefly: ignore [missing-import]
from django.db.models.signals import post_save
# pyrefly: ignore [missing-import]
from django.dispatch import receiver
# pyrefly: ignore [missing-import]
from django.db.models import Avg

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, max_length=500)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

    @property
    def total_attempts_count(self):
        return self.user.attempts.filter(completed_at__isnull=False).count()

    @property
    def completed_attempts(self):
        return self.user.attempts.filter(completed_at__isnull=False)

    @property
    def completed_attempts_count(self):
        return self.completed_attempts.count()

    @property
    def average_score(self):
        avg = self.completed_attempts.aggregate(Avg('percentage'))['percentage__avg']
        return round(avg, 2) if avg is not None else 0.0

    @property
    def pass_rate(self):
        total = self.completed_attempts_count
        if total == 0:
            return 0.0
        passed = self.completed_attempts.filter(status='Passed').count()
        return round((passed / total) * 100, 2)

    @property
    def category_stats(self):
        """Returns performance stats grouped by quiz category."""
        attempts = self.completed_attempts
        categories_config = {
            'Programming': {'icon': 'code', 'color': '#3b82f6', 'gradient': '#3b82f6, #6366f1'},
            'Science': {'icon': 'atom', 'color': '#ec4899', 'gradient': '#ec4899, #d946ef'},
            'Mathematics': {'icon': 'calculator', 'color': '#10b981', 'gradient': '#10b981, #14b8a6'},
            'General Knowledge': {'icon': 'globe', 'color': '#f59e0b', 'gradient': '#f59e0b, #eab308'},
            'Aptitude': {'icon': 'brain', 'color': '#f43f5e', 'gradient': '#f43f5e, #f43f5e'},
            'History': {'icon': 'monument', 'color': '#d97706', 'gradient': '#d97706, #f59e0b'},
            'Literature': {'icon': 'book-open', 'color': '#8b5cf6', 'gradient': '#8b5cf6, #a78bfa'},
            'Sports': {'icon': 'trophy', 'color': '#2563eb', 'gradient': '#2563eb, #3b82f6'},
        }
        stats = {}
        for cat, cfg in categories_config.items():
            cat_attempts = attempts.filter(quiz__category=cat)
            count = cat_attempts.count()
            if count > 0:
                avg = cat_attempts.aggregate(Avg('percentage'))['percentage__avg']
                passed = cat_attempts.filter(status='Passed').count()
                stats[cat] = {
                    'count': count,
                    'avg_score': round(avg, 2) if avg is not None else 0.0,
                    'passed': passed,
                    'pass_rate': round((passed / count) * 100, 2),
                    'icon': cfg['icon'],
                    'color': cfg['color'],
                    'gradient': cfg['gradient'],
                }
            else:
                stats[cat] = {
                    'count': 0,
                    'avg_score': 0.0,
                    'passed': 0,
                    'pass_rate': 0.0,
                    'icon': cfg['icon'],
                    'color': cfg['color'],
                    'gradient': cfg['gradient'],
                }
        return stats

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()


class Quiz(models.Model):
    CATEGORY_CHOICES = [
        ('Programming', 'Programming'),
        ('Science', 'Science'),
        ('Mathematics', 'Mathematics'),
        ('General Knowledge', 'General Knowledge'),
        ('Aptitude', 'Aptitude'),
        ('History', 'History'),
        ('Literature', 'Literature'),
        ('Sports', 'Sports'),
    ]

    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    time_limit = models.PositiveIntegerField(help_text="Time limit in minutes")
    pass_mark = models.PositiveIntegerField(default=50, help_text="Minimum percentage required to pass (e.g. 50)")
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Quizzes"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.category})"


class Question(models.Model):
    OPTION_CHOICES = [
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D'),
    ]

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1, choices=OPTION_CHOICES)
    explanation = models.TextField(blank=True, null=True, help_text="Explanation shown to users after submission")

    def __str__(self):
        return f"Q: {self.question_text[:50]}... ({self.quiz.title})"


class QuizAttempt(models.Model):
    STATUS_CHOICES = [
        ('Passed', 'Passed'),
        ('Failed', 'Failed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attempts')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='attempts')
    score = models.PositiveIntegerField(default=0, help_text="Number of correct answers")
    percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    time_taken = models.PositiveIntegerField(blank=True, null=True, help_text="Time taken in seconds")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Failed')

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} ({self.status})"

    @property
    def time_taken_formatted(self):
        if self.time_taken is None:
            return "0s"
        minutes = self.time_taken // 60
        seconds = self.time_taken % 60
        if minutes > 0:
            return f"{minutes}m {seconds}s"
        return f"{seconds}s"

    class Meta:
        ordering = ['-started_at']


class UserAnswer(models.Model):
    OPTION_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=1, choices=OPTION_CHOICES, blank=True, null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Attempt {self.attempt.id} | Question {self.question.id} | Selected: {self.selected_option}"
