from django.shortcuts import render,get_object_or_404,redirect #template에 적용하여 HTML로 반환하는 함수, not found
from django.utils import timezone
from .models import Question,Answer
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponseNotAllowed
from django.core.paginator import Paginator

def index(request):
    page= request.GET.get('page','1') #페이지
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST) #request.POST에 담긴 (subject,content)가 QuestionForm의 속성에 자동으로 저장
        if form.is_valid(): #form이 유효한지 검사
            question = form.save(commit=False) #Question 데이터를 저장, commit=False : 임시저장
            question.author = request.user
            question.create_date = timezone.now() #create_date 값 설정
            question.save() #저장
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author=request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)