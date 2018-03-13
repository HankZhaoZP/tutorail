from django.shortcuts import render, get_list_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Questions, Choice

# Create your views here.


def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', context={
        'latest_question_list': latest_question_list,
    })


def detail(request, question_id):
    question = get_list_or_404(Questions, pk=question_id)
    return render(request, 'polls/detail.html', context={
        'question': question,
    })


def result(request, question_id):
    question = get_list_or_404(Questions, pk=question_id)
    return render(request, 'polls/result.html', context={
        'question': question,
    })


def vote(request, question_id):
    question = get_list_or_404(Questions, pk=question_id)
    try:
        selected_choiced = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html', context= {
            'question': question,
            'error_message': "You didn't select a choice",
        })

    else:
        selected_choiced.votes += 1
        selected_choiced.save()
        # 如果有post数据成功的情况，用HttpResponseRedirect返回页面，
        # 防止用户点击返回导致post2次数据
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

