# Modern Online Quiz Application

A responsive online quiz platform built using Python, Django, vanilla JavaScript, HTML5, custom CSS3, and MySQL.

The application functions as a modern educational SaaS platform with dark-themed glassmorphism elements, CSS animations, visual countdown dials, interactive question navigators, and a profile proficiency chart.

---

## Key Features

1. **User Authentication & Profiles**:
   - Secure registration, login, and logout.
   - Profile settings to edit username, email, and biography.
   - Dynamic competency graphs displaying the user's average score across different learning tracks.

2. **Quiz Catalog**:
   - Filter quizzes by Category (Programming, Science, Mathematics, GK, Aptitude) and Difficulty (Easy, Medium, Hard).
   - Real-time text search for quiz titles and descriptions.
   - High score tracking and passed/failed badges for attempted quizzes.

3. **Interactive Timed Quiz Workspace**:
   - Distraction-free single-question slider layout.
   - Clickable option choice cards with smooth active state transitions.
   - SVG-based circular countdown timer that turns red and pulses when time is below 20% remaining.
   - **sessionStorage-based answer caching** to prevent data loss on page refreshes.
   - Interactive Question Navigator grid representing Active, Answered, Skipped, and Unanswered questions.
   - Warnings modal triggered on submission if questions are left unanswered.
   - Safe timing validations on the Django backend to prevent client-side clock tampering.

4. **Results Dashboard & Review**:
   - Scoring details showing raw correctness ratios, percentages, time taken, and correct/incorrect/skipped metrics.
   - Custom SVG score gauge with dynamic loading/stroke-offset animations.
   - Correct answer reviews with explanation cards showing the detailed reasoning behind every correct choice.

5. **Historical Attempt Log**:
   - Filter history logs by category, date range, and passing status.
   - Comprehensive performance aggregates (Total Completed, Average Score, Pass Rate).

6. **Admin Inline Quiz Editor**:
   - Add/edit quizzes and questions directly in line on the standard Django Admin interface.

---

## Technology Stack

- **Backend**: Python 3.13+ with Django 5.0
- **Database**: SQLite (default local fallback) or MySQL (fully supported via `.env`)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript, FontAwesome Icons

---

## Installation & Local Setup

The project includes an automatic **Twelve-Factor fallback mechanism**: by default, the app is pre-configured to run on a local SQLite database (`db.sqlite3`), making it instantly runnable.

### 1. Setup Virtual Environment
Run the following commands inside the project root:
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows Powershell)
.\.venv\Scripts\Activate.ps1

# Install required dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables
A default `.env` file is already created in your workspace. You can customize the settings using `.env.example` as a guide:
```ini
# Django Settings
DEBUG=True
SECRET_KEY=django-insecure-quiz-app-development-secret-key-39d440bd
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration (Set to 'mysql' to use MySQL, 'sqlite' is default)
DB_TYPE=sqlite
```

### 3. Generate and Apply Database Migrations
Set up database schemas for authorization, session logs, and quiz entities:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Seed Sample Quizzes
Seed the database with 5 pre-made quizzes and 25 questions across Programming, Science, Mathematics, GK, and Aptitude:
```bash
python manage.py seed_quizzes
```

### 5. Create Superuser (Admin Account)
A default superuser is pre-created by the setup commands:
- **Username**: `admin`
- **Password**: `adminpassword123`

To create another custom admin account:
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
Launch the server locally:
```bash
python manage.py run_server
# or
python manage.py runserver
```

Open your browser and navigate to:
- **Web App**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Configuring MySQL

To connect the application to a MySQL database instead of SQLite:

1. Ensure a MySQL database server is running locally or in your deployment environment.
2. Log into MySQL and create a database:
   ```sql
   CREATE DATABASE quiz_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
3. Update your `.env` file parameters:
   ```ini
   DB_TYPE=mysql
   DB_NAME=quiz_db
   DB_USER=root
   DB_PASSWORD=your_mysql_password
   DB_HOST=127.0.0.1
   DB_PORT=3306
   ```
4. Re-run migrations and seed the database:
   ```bash
   python manage.py migrate
   python manage.py seed_quizzes
   ```

*Note: The project uses PyMySQL (`pymysql`), a pure Python MySQL driver, which runs seamlessly on Windows and does not require complex C++ compile tools.*

---

## Production Email & Password Reset Setup (Render)

To enable real password reset emails on Render:

1. Open your **Render Dashboard** -> Select your Web Service -> **Environment**.
2. Add the following environment variables:
   - `EMAIL_BACKEND`: `django.core.mail.backends.smtp.EmailBackend`
   - `EMAIL_HOST`: `smtp.gmail.com` *(or your SMTP host, e.g., Brevo/SendGrid)*
   - `EMAIL_PORT`: `587`
   - `EMAIL_USE_TLS`: `True`
   - `EMAIL_HOST_USER`: `your-email@gmail.com`
   - `EMAIL_HOST_PASSWORD`: `your-16-character-app-password`
   - `DEFAULT_FROM_EMAIL`: `Quiznapse <your-email@gmail.com>`

*Tip for Gmail:* Turn on 2-Factor Authentication on your Google account, then generate an **App Password** under Google Account Security settings to use as `EMAIL_HOST_PASSWORD`.

