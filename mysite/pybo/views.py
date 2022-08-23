from django.shortcuts import render,get_object_or_404 #template에 적용하여 HTML로 반환하는 함수, not found
from .models import Question


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)