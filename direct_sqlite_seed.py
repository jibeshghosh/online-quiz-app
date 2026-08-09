import sqlite3
import datetime
import os
import sys

db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
print(f"Connecting directly to SQLite DB at: {db_path}")

# Add workspace to sys.path to import ALL_QUIZZES_DATA
sys.path.insert(0, os.path.dirname(__file__))
from quizzes.quiz_data import ALL_QUIZZES_DATA

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Clear existing questions, quizzes, user answers, and attempts
cursor.execute("DELETE FROM quizzes_useranswer;")
cursor.execute("DELETE FROM quizzes_quizattempt;")
cursor.execute("DELETE FROM quizzes_question;")
cursor.execute("DELETE FROM quizzes_quiz;")

now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

quiz_id_counter = 1
question_id_counter = 1
quiz_count = 0
question_count = 0

for category_name, topics in ALL_QUIZZES_DATA.items():
    for topic_title, topic_data in topics.items():
        current_quiz_id = quiz_id_counter
        quiz_id_counter += 1
        
        cursor.execute("""
            INSERT INTO quizzes_quiz (id, title, description, category, difficulty, time_limit, pass_mark, is_published, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            current_quiz_id,
            topic_title,
            topic_data['description'],
            category_name,
            topic_data['difficulty'],
            topic_data['time_limit'],
            topic_data['pass_mark'],
            1,
            now_str
        ))
        quiz_count += 1
        
        for q_tuple in topic_data['questions']:
            current_q_id = question_id_counter
            question_id_counter += 1
            
            cursor.execute("""
                INSERT INTO quizzes_question (id, quiz_id, question_text, option_a, option_b, option_c, option_d, correct_option, explanation)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                current_q_id,
                current_quiz_id,
                q_tuple[0],
                q_tuple[1],
                q_tuple[2],
                q_tuple[3],
                q_tuple[4],
                q_tuple[5],
                q_tuple[6]
            ))
            question_count += 1

conn.commit()
conn.close()
print(f"[DIRECT SQLITE SUCCESS] Directly inserted {quiz_count} quizzes and {question_count} topic-matched questions into {db_path}!")
