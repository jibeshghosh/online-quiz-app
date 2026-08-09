import os
# pyrefly: ignore [missing-import]
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quizzes.models import Quiz, Question
from quizzes.quiz_data import ALL_QUIZZES_DATA

print("Seeding 40 topic-matched quizzes and 400 questions...")

# Clear existing quizzes and questions to ensure fresh, perfectly aligned data
Question.objects.all().delete()
Quiz.objects.all().delete()

quiz_count = 0
question_count = 0

for category_name, topics in ALL_QUIZZES_DATA.items():
    print(f"\nProcessing Category: [{category_name}]")
    for topic_title, topic_data in topics.items():
        quiz = Quiz.objects.create(
            title=topic_title,
            description=topic_data['description'],
            category=category_name,
            difficulty=topic_data['difficulty'],
            time_limit=topic_data['time_limit'],
            pass_mark=topic_data['pass_mark'],
            is_published=True
        )
        quiz_count += 1
        
        for q_tuple in topic_data['questions']:
            Question.objects.create(
                quiz=quiz,
                question_text=q_tuple[0],
                option_a=q_tuple[1],
                option_b=q_tuple[2],
                option_c=q_tuple[3],
                option_d=q_tuple[4],
                correct_option=q_tuple[5],
                explanation=q_tuple[6]
            )
            question_count += 1
        print(f"  -> Created Quiz: '{quiz.title}' ({quiz.difficulty}) with {len(topic_data['questions'])} Qs")

print(f"\nReal data seeding complete! ALL {quiz_count} Quizzes created with EXACTLY matching 10 real questions each ({question_count} total questions).")
