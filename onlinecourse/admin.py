from django.contrib import admin
# أضفنا الموديلات الناقصة في سطر الـ import
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

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
    list_display = ['title'] # شلنا order لو مش موجود في الموديل عشان ما يعلق

# 5. تخصيص لوحة إدارة الدورة
class CourseAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

# تسجيل كل النماذج (تأكد من تسجيل الموديلات السبعة المطلوبة)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Instructor) # مهم جداً للصورة
admin.site.register(Learner)    # مهم جداً للصورة
admin.site.register(Submission) # مهم جداً للصورة