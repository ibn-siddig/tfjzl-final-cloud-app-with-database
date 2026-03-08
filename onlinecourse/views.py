from django.shortcuts import render, get_object_or_404
from .models import Course, Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse

# دالة عرض تفاصيل الكورس (تأكد من وجودها للسؤال 4 و 5)
def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'onlinecourse/course_detail_bootstrap.html', {'course': course})

# دالة الـ submit المعدلة لعرض التهنئة في نفس الصفحة
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # الحصول على قائمة معرفات الخيارات التي اختارها الطالب
        selected_ids = request.POST.getlist('choice')
        total_score = 0
        
        # جلب كل الأسئلة المرتبطة بهذا الكورس
        questions = Question.objects.filter(course=course)
        max_score = questions.count() # إجمالي عدد الأسئلة
        
        for question in questions:
            # جلب الخيارات الصحيحة لهذا السؤال فقط
            correct_choices = question.choice_set.filter(is_correct=True)
            # جلب اختيارات الطالب التي تنتمي لهذا السؤال
            user_choices_for_q = [int(id) for id in selected_ids if int(id) in question.choice_set.values_list('id', flat=True)]
            
            # إذا تطابقت اختيارات الطالب تماماً مع الاختيارات الصحيحة (ولم تكن القائمة فارغة)
            if user_choices_for_q and set(user_choices_for_q) == set(correct_choices.values_list('id', flat=True)):
                total_score += 1
                
        # إرسال النتيجة لنفس صفحة التفاصيل لعرض رسالة التهنئة
        context = {
            'course': course,
            'grade': total_score,
            'total_score': max_score
        }
        # بننادي نفس ملف الـ HTML اللي ضفنا فيه كلمة Congratulations
        return render(request, 'onlinecourse/course_detail_bootstrap.html', context)
    
    return HttpResponseRedirect(reverse('onlinecourse:course_details', args=(course.id,)))