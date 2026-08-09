# pyrefly: ignore [missing-import]
from django.apps import AppConfig
import sys

class QuizzesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quizzes'

    def ready(self):
        # Skip during management commands
        if any(cmd in sys.argv for cmd in ['makemigrations', 'migrate', 'collectstatic', 'test']):
            return
            
        try:
            from quizzes.models import Quiz, Question
            sample_q = Question.objects.filter(quiz__title='Python Fundamentals').first()
            if Quiz.objects.count() != 40 or Question.objects.count() != 400 or not sample_q or sample_q.question_text != "What is the output of print(2 ** 3) in Python?":
                print("[AUTO-SYNC] Outdated DB detected. Running direct SQLite database seeding...")
                import direct_sqlite_seed
        except Exception as e:
            print(f"[AUTO-SYNC ERROR] {e}")
            pass
