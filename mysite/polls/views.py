from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F

from .models import Question, Choice

def index(request):

	latest_question_list = Question.objects.order_by('-pub_date')[:5]

	context = {
		'latest_question_list': latest_question_list,
	}

	return render(request, 'polls/index.html', context)


def detail(request, question_id):

	question = get_object_or_404(Question, pk=question_id)

	return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):

	question = get_object_or_404(Question, pk=question_id)
	try:
		select_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		select_choice.votes = F('votes') + 1 
		#poderia usar += 1, porém haveria problemas de concorrência caso dois usuarios tentasse votar ao mesmo tempo, a função F previne esse problema.
		select_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):

	question = get_object_or_404(Question, pk=question_id)

	return render(request, 'polls/results.html', {'question': question})
