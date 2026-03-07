from django.contrib import admin
from .models import Course, Lesson, Question, Choice

# 1. تعريف كيف ستظهر الخيارات (Choices) تحت السؤال مباشرة
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

# 2. تعريف كيف ستظهر الأسئلة (Questions) تحت الدورة مباشرة
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

# 3. تخصيص لوحة إدارة الأسئلة
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'course', 'grade']

# 4. تخصيص لوحة إدارة الدروس
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']

# 5. تخصيص لوحة إدارة الدورة (لربط كل شيء ببعضه)
class CourseAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

# تسجيل النماذج في لوحة الإدارة (Registration)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)