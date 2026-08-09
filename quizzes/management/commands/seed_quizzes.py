# pyrefly: ignore [missing-import]
from django.core.management.base import BaseCommand
from quizzes.models import Quiz, Question
from quizzes.quiz_data import ALL_QUIZZES_DATA

class Command(BaseCommand):
    help = 'Seeds the database with 40 topic-matched quizzes and 400 MCQ questions across 8 categories'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding 40 topic-matched quizzes and 400 questions...')

        # Clear existing quizzes and questions to ensure fresh, perfectly aligned data
        Question.objects.all().delete()
        Quiz.objects.all().delete()

        quiz_count = 0
        question_count = 0

        for category_name, topics in ALL_QUIZZES_DATA.items():
            self.stdout.write(f"\nSeeding Category: [{category_name}]")
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
                self.stdout.write(f"  -> Created Quiz: '{quiz.title}' ({quiz.difficulty}) with {len(topic_data['questions'])} Qs")

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully seeded {quiz_count} quizzes and {question_count} topic-matched questions across all 8 categories!'))
