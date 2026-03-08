from django.shortcuts import render, get_object_or_404
from .models import Course, Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse


def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'onlinecourse/course_detail_bootstrap.html', {'course': course})


def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == 'POST':
        selected_ids = request.POST.getlist('choice')
        total_score = 0

        questions = Question.objects.filter(course=course)
        max_score = questions.count()

        for question in questions:
            correct_choices = question.choice_set.filter(is_correct=True)

            user_choices_for_q = [
                int(id) for id in selected_ids
                if int(id) in question.choice_set.values_list('id', flat=True)
            ]

            if user_choices_for_q and set(user_choices_for_q) == set(correct_choices.values_list('id', flat=True)):
                total_score += 1

        context = {
            'course': course,
            'grade': total_score,
            'total_score': max_score
        }

        return render(request, 'onlinecourse/course_detail_bootstrap.html', context)

    return HttpResponseRedirect(reverse('onlinecourse:course_details', args=(course.id,)))


def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course
    }

    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)