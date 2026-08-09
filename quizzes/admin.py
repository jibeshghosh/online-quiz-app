# pyrefly: ignore [missing-import]
from django.contrib import admin
from .models import Quiz, Question, QuizAttempt, UserAnswer, UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'completed_attempts_count', 'average_score', 'pass_rate')
    search_fields = ('user__username', 'user__email', 'bio')


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    fields = ('question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option', 'explanation')


class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'difficulty', 'time_limit', 'pass_mark', 'is_published', 'created_at')
    list_filter = ('category', 'difficulty', 'is_published')
    search_fields = ('title', 'description')
    inlines = [QuestionInline]
    actions = ['publish_quizzes', 'unpublish_quizzes']

    def publish_quizzes(self, request, queryset):
        queryset.update(is_published=True)
        self.message_user(request, "Selected quizzes have been published.")
    publish_quizzes.short_description = "Publish selected quizzes"

    def unpublish_quizzes(self, request, queryset):
        queryset.update(is_published=False)
        self.message_user(request, "Selected quizzes have been unpublished.")
    unpublish_quizzes.short_description = "Unpublish selected quizzes"


class UserAnswerInline(admin.TabularInline):
    model = UserAnswer
    extra = 0
    readonly_fields = ('question', 'selected_option', 'is_correct')
    can_delete = False


class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'percentage', 'status', 'started_at', 'completed_at', 'time_taken')
    list_filter = ('status', 'quiz__category', 'quiz__difficulty')
    search_fields = ('user__username', 'quiz__title')
    readonly_fields = ('started_at',)
    inlines = [UserAnswerInline]


# Register all models with the Admin Site
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(QuizAttempt, QuizAttemptAdmin)
admin.site.register(UserAnswer)

# Customize Admin Site Text
admin.site.site_header = "Admin Login"
admin.site.site_title = "Admin Login"
admin.site.index_title = "Welcome to Quiznapse Admin Portal"

