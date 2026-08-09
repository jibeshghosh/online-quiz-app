# pyrefly: ignore [missing-import]
from django.shortcuts import render, redirect, get_object_or_404
# pyrefly: ignore [missing-import]
from django.contrib.auth import login, authenticate, logout
# pyrefly: ignore [missing-import]
from django.contrib.auth.decorators import login_required
# pyrefly: ignore [missing-import]
from django.contrib.auth.models import User
# pyrefly: ignore [missing-import]
from django.contrib import messages
# pyrefly: ignore [missing-import]
from django.utils import timezone
# pyrefly: ignore [missing-import]
from django.db.models import Q, Avg
from decimal import Decimal

from .models import Quiz, Question, QuizAttempt, UserAnswer
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
# pyrefly: ignore [missing-import]
from django.contrib.auth.forms import AuthenticationForm

def ensure_curated_quizzes_loaded():
    """Ensures database contains the exact 400 topic-matched questions for all 40 quizzes."""
    try:
        from .quiz_data import ALL_QUIZZES_DATA
        sample_q = Question.objects.filter(quiz__title='Python Fundamentals').first()
        if Quiz.objects.count() != 40 or Question.objects.count() != 400 or not sample_q or sample_q.question_text != "What is the output of print(2 ** 3) in Python?":
            UserAnswer.objects.all().delete()
            QuizAttempt.objects.all().delete()
            Question.objects.all().delete()
            Quiz.objects.all().delete()
            
            for category_name, topics in ALL_QUIZZES_DATA.items():
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
    except Exception:
        pass


def landing(request):
    """Public landing page."""
    ensure_curated_quizzes_loaded()
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    # Get statistics to display on the landing page
    stats = {
        'total_quizzes': Quiz.objects.filter(is_published=True).count(),
        'total_questions': Question.objects.count(),
        'total_users': User.objects.count(),
        'total_attempts': QuizAttempt.objects.filter(completed_at__isnull=False).count(),
    }
    return render(request, 'quizzes/landing.html', {'stats': stats})


def register(request):
    """User registration page."""
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, f"Welcome to Quiznapse, {user.first_name}! Your account has been created.")
            return redirect('dashboard')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = RegistrationForm()
        
    return render(request, 'quizzes/register.html', {'form': form})


def login_view(request):
    """User login page."""
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.first_name}!")
                next_url = request.GET.get('next', 'dashboard')
                return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
        
    return render(request, 'quizzes/login.html', {'form': form})


def logout_view(request):
    """User logout."""
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('landing')


@login_required
def dashboard(request):
    """User dashboard showing stats, categories and recent attempts."""
    ensure_curated_quizzes_loaded()
    profile = request.user.profile
    recent_attempts = QuizAttempt.objects.filter(
        user=request.user, 
        completed_at__isnull=False
    ).order_by('-completed_at')[:5]
    
    # Get total published quizzes count
    published_quizzes_count = Quiz.objects.filter(is_published=True).count()
    
    # Get categories stats
    categories = [
        {'name': 'Programming', 'icon': 'code', 'gradient': 'from-blue-600 to-indigo-600', 'desc': 'Python, JavaScript, databases, and logic.'},
        {'name': 'Science', 'icon': 'atom', 'gradient': 'from-purple-600 to-pink-600', 'desc': 'Physics, chemistry, biology, and space.'},
        {'name': 'Mathematics', 'icon': 'calculator', 'gradient': 'from-emerald-600 to-teal-600', 'desc': 'Algebra, calculus, statistics, and theory.'},
        {'name': 'General Knowledge', 'icon': 'globe', 'gradient': 'from-amber-600 to-orange-600', 'desc': 'History, geography, world events, and culture.'},
        {'name': 'Aptitude', 'icon': 'brain', 'gradient': 'from-red-600 to-rose-600', 'desc': 'Logical reasoning, quantitative, and verbal skills.'},
        {'name': 'History', 'icon': 'monument', 'gradient': 'from-amber-800 to-yellow-600', 'desc': 'World history, ancient civilizations, and historical events.'},
        {'name': 'Literature', 'icon': 'book-open', 'gradient': 'from-violet-600 to-purple-600', 'desc': 'Famous authors, literary classics, and poetry.'},
        {'name': 'Sports', 'icon': 'trophy', 'gradient': 'from-blue-600 to-teal-500', 'desc': 'World sports, olympics, rules, and athletic history.'},
    ]

    for cat in categories:
        cat['count'] = Quiz.objects.filter(category=cat['name'], is_published=True).count()
        cat['completed_count'] = QuizAttempt.objects.filter(
            user=request.user, 
            quiz__category=cat['name'], 
            completed_at__isnull=False
        ).count()
        
    context = {
        'profile': profile,
        'recent_attempts': recent_attempts,
        'categories': categories,
        'published_quizzes_count': published_quizzes_count,
    }
    return render(request, 'quizzes/dashboard.html', context)


@login_required
def quiz_list(request):
    """Catalog of available quizzes with filter and search."""
    ensure_curated_quizzes_loaded()
    search_query = request.GET.get('search', '').strip()
    category_filter = request.GET.get('category', '')
    difficulty_filter = request.GET.get('difficulty', '')
    
    quizzes = Quiz.objects.filter(is_published=True)
    
    if search_query:
        quizzes = quizzes.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    if category_filter:
        quizzes = quizzes.filter(category=category_filter)
    if difficulty_filter:
        quizzes = quizzes.filter(difficulty=difficulty_filter)
        
    categories = [choice[0] for choice in Quiz.CATEGORY_CHOICES]
    difficulties = [choice[0] for choice in Quiz.DIFFICULTY_CHOICES]
    
    # For each quiz, check if the user has attempted it and their high score
    for quiz in quizzes:
        attempts = QuizAttempt.objects.filter(user=request.user, quiz=quiz, completed_at__isnull=False)
        quiz.attempts_count = attempts.count()
        if quiz.attempts_count > 0:
            quiz.high_score = attempts.order_by('-percentage').first().percentage
            quiz.last_status = attempts.order_by('-completed_at').first().status
        else:
            quiz.high_score = None
            quiz.last_status = None
            
    context = {
        'quizzes': quizzes,
        'categories': categories,
        'difficulties': difficulties,
        'search_query': search_query,
        'category_filter': category_filter,
        'difficulty_filter': difficulty_filter,
    }
    return render(request, 'quizzes/quiz_list.html', context)


@login_required
def quiz_detail(request, quiz_id):
    """Quiz instructions/details page."""
    quiz = get_object_or_404(Quiz, id=quiz_id, is_published=True)
    questions_count = quiz.questions.count()
    
    # Previous attempts for this specific quiz
    attempts = QuizAttempt.objects.filter(
        user=request.user, 
        quiz=quiz, 
        completed_at__isnull=False
    ).order_by('-completed_at')
    
    context = {
        'quiz': quiz,
        'questions_count': questions_count,
        'attempts': attempts,
    }
    return render(request, 'quizzes/quiz_detail.html', context)


@login_required
def quiz_attempt(request, quiz_id):
    """Renders the timed quiz screen, resuming or creating an attempt."""
    quiz = get_object_or_404(Quiz, id=quiz_id, is_published=True)
    questions = quiz.questions.all()
    
    if not questions.exists():
        messages.error(request, "This quiz has no questions yet.")
        return redirect('quiz_detail', quiz_id=quiz.id)
        
    now = timezone.now()
    time_limit_seconds = quiz.time_limit * 60
    
    # Check if there is an active incomplete attempt
    attempt = QuizAttempt.objects.filter(
        user=request.user,
        quiz=quiz,
        completed_at__isnull=True
    ).order_by('-started_at').first()
    
    if attempt:
        # Check if the active attempt has already expired
        elapsed = (now - attempt.started_at).total_seconds()
        if elapsed > time_limit_seconds + 30: # 30s grace period
            # Close the expired attempt as Failed
            attempt.completed_at = attempt.started_at + timezone.timedelta(seconds=time_limit_seconds)
            attempt.time_taken = time_limit_seconds
            attempt.status = 'Failed'
            attempt.save()
            # Start a new attempt
            attempt = QuizAttempt.objects.create(user=request.user, quiz=quiz)
            elapsed = 0.0
    else:
        # Create a new attempt
        attempt = QuizAttempt.objects.create(user=request.user, quiz=quiz)
        elapsed = 0.0
        
    # Calculate time remaining
    time_remaining_seconds = max(0, int(time_limit_seconds - elapsed))
    
    context = {
        'quiz': quiz,
        'questions': questions,
        'attempt': attempt,
        'time_remaining': time_remaining_seconds,
        'time_limit_seconds': time_limit_seconds,
    }
    return render(request, 'quizzes/quiz_attempt.html', context)


@login_required
def quiz_submit(request, attempt_id):
    """Processes answers, grades the attempt, and saves result."""
    attempt = get_object_or_404(QuizAttempt, id=attempt_id, user=request.user, completed_at__isnull=True)
    quiz = attempt.quiz
    questions = quiz.questions.all()
    
    if request.method == 'POST':
        now = timezone.now()
        attempt.completed_at = now
        
        # Calculate time taken
        time_taken = (now - attempt.started_at).total_seconds()
        time_limit_seconds = quiz.time_limit * 60
        
        # Cap time taken in case of network latency or timer overflow
        if time_taken > time_limit_seconds + 30:
            time_taken = time_limit_seconds + 10
            
        attempt.time_taken = int(time_taken)
        
        score = 0
        total_questions = questions.count()
        
        # Grade answers
        for q in questions:
            selected = request.POST.get(f'question_{q.id}') # Returns 'A', 'B', 'C', 'D' or None
            
            is_correct = False
            if selected:
                is_correct = (selected == q.correct_option)
                if is_correct:
                    score += 1
                    
            UserAnswer.objects.create(
                attempt=attempt,
                question=q,
                selected_option=selected,
                is_correct=is_correct
            )
            
        percentage = (Decimal(score) / Decimal(total_questions)) * 100 if total_questions > 0 else Decimal(0)
        percentage = round(percentage, 2)
        
        attempt.score = score
        attempt.percentage = percentage
        attempt.status = 'Passed' if percentage >= quiz.pass_mark else 'Failed'
        attempt.save()
        
        messages.success(request, f"Quiz submitted successfully! You scored {score}/{total_questions} ({percentage}%).")
        return redirect('quiz_result', attempt_id=attempt.id)
        
    return redirect('dashboard')


@login_required
def quiz_result(request, attempt_id):
    """Displays results summary dashboard with SVG circular indicator."""
    attempt = get_object_or_404(QuizAttempt, id=attempt_id, user=request.user)
    
    # Get answer stats
    answers = attempt.answers.all()
    correct_count = answers.filter(is_correct=True).count()
    total_count = attempt.quiz.questions.count()
    skipped_count = answers.filter(selected_option__isnull=True).count() + answers.filter(selected_option='').count()
    incorrect_count = total_count - correct_count - skipped_count
    
    # Calculate display time taken
    minutes = attempt.time_taken // 60
    seconds = attempt.time_taken % 60
    time_taken_str = f"{minutes}m {seconds}s" if minutes > 0 else f"{seconds}s"
    
    context = {
        'attempt': attempt,
        'correct': correct_count,
        'incorrect': incorrect_count,
        'skipped': skipped_count,
        'total': total_count,
        'time_taken_str': time_taken_str,
    }
    return render(request, 'quizzes/quiz_result.html', context)


@login_required
def quiz_review(request, attempt_id):
    """Allows step-by-step verification of quiz answers, explanations and correction status."""
    attempt = get_object_or_404(QuizAttempt, id=attempt_id, user=request.user)
    user_answers = {ua.question_id: ua for ua in attempt.answers.all()}
    
    questions = attempt.quiz.questions.all()
    for q in questions:
        q.user_answer = user_answers.get(q.id)
        
    context = {
        'attempt': attempt,
        'questions': questions,
    }
    return render(request, 'quizzes/quiz_review.html', context)


@login_required
def my_results(request):
    """Personal attempts log with interactive category and status filters."""
    category_filter = request.GET.get('category', '')
    status_filter = request.GET.get('status', '')
    date_filter = request.GET.get('date', '')
    
    attempts = QuizAttempt.objects.filter(user=request.user, completed_at__isnull=False)
    
    if category_filter:
        attempts = attempts.filter(quiz__category=category_filter)
    if status_filter:
        attempts = attempts.filter(status=status_filter)
        
    if date_filter == 'today':
        attempts = attempts.filter(completed_at__date=timezone.now().date())
    elif date_filter == 'week':
        attempts = attempts.filter(completed_at__gte=timezone.now() - timezone.timedelta(days=7))
    elif date_filter == 'month':
        attempts = attempts.filter(completed_at__gte=timezone.now() - timezone.timedelta(days=30))
        
    categories = [choice[0] for choice in Quiz.CATEGORY_CHOICES]
    
    # Calculate cumulative stats for the history page
    total_completed = attempts.count()
    total_passed = attempts.filter(status='Passed').count()
    avg_score = attempts.aggregate(Avg('percentage'))['percentage__avg']
    avg_score = round(avg_score, 2) if avg_score is not None else 0.0
    
    context = {
        'attempts': attempts,
        'categories': categories,
        'category_filter': category_filter,
        'status_filter': status_filter,
        'date_filter': date_filter,
        'stats': {
            'total_completed': total_completed,
            'total_passed': total_passed,
            'avg_score': avg_score,
            'pass_rate': round((total_passed / total_completed * 100), 2) if total_completed > 0 else 0.0
        }
    }
    return render(request, 'quizzes/my_results.html', context)


@login_required
def profile(request):
    """User profile metrics page with profile editing."""
    user = request.user
    profile = user.profile
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, instance=profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your profile settings have been updated successfully!")
            return redirect('profile')
        else:
            messages.error(request, "Failed to update profile. Please verify your details.")
    else:
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileUpdateForm(instance=profile)
        
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'profile': profile,
    }
    return render(request, 'quizzes/profile.html', context)


def social_auth_mock(request, provider):
    """Simulates social OAuth logins (Google, GitHub) for local testing without external credentials."""
    provider = provider.lower()
    username = f"{provider}_user"
    email = f"{provider}_user@quiznapse.com"
    first_name = "GitHub" if provider == "github" else provider.capitalize()
    last_name = "Auth User"
    
    # Retrieve or create simulated user
    user = User.objects.filter(username=username).first()
    if not user:
        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=User.objects.make_random_password()
        )
        # Update user profile bio for mock user
        profile = user.profile
        profile.bio = f"Automated test account generated via {first_name} OAuth authentication."
        profile.save()
        
    # Log user in
    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    messages.success(request, f"Successfully authenticated via {first_name}! Welcome to Quiznapse.")
    return redirect('dashboard')


def oauth_choose_account(request, provider='google'):
    """Renders a simulated account chooser page mimicking Google or GitHub sign-in pages."""
    provider = provider.lower()
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name', 'Social User')
        username = email.split('@')[0]
        
        user = User.objects.filter(username=username).first()
        if not user:
            first_name = name.split(' ')[0]
            last_name = name.split(' ')[1] if len(name.split(' ')) > 1 else ''
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=User.objects.make_random_password()
            )
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, f"Successfully authenticated via {provider.capitalize()}!")
        return redirect('dashboard')
        
    context = {
        'provider': provider,
        'provider_title': 'Google' if provider == 'google' else 'GitHub',
    }
    return render(request, 'quizzes/oauth_choose.html', context)






