from django.shortcuts import render, get_object_or_404
# from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }  # a dictionary mapping template variable names to Python objects
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)



# todo: 아래의 def 모두 httpresponse -> render 로 변경
def detail(request, question_id):
    # 1)
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    # 2)
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = request.POST['choice']  # request.POST.get()
        selected_choice = question.choice_set.get(pk=choice)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))