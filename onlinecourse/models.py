from django.db import models
from django.conf import settings
from django.utils import timezone

# نموذج الدورة الأساسي
class Course(models.Model):
    name = models.CharField(null=False, max_length=100, default='online course')
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='course_images/')
    pub_date = models.DateField(null=True)

    def __str__(self):
        return self.name

# نموذج الحصة (Lesson)
class Lesson(models.Model):
    title = models.CharField(max_length=200, default="title")
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()

# نموذج التسجيل (Enrollment)
class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(default=timezone.now)

# --- الجبايات المطلوبة للمشروع النهائي (Task 1) ---

# 1. نموذج السؤال (Question)
class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=5)

    def __str__(self):
        return self.question_text

# 2. نموذج الخيار (Choice)
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

# 3. نموذج التقديم (Submission)
class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)