from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import Question, Choice
from django.utils import timezone
from django.http import HttpResponseRedirect
#template view to test static files and templates






#polls list view
#List all the polls here

class Index(ListView):
    model = Question
    template_name = "polls/index.html"
    context_object_name = 'latest_questions'
    
    def get_queryset(self):
        return  Question.objects.filter(
        published_at__lte=timezone.now()).order_by('-published_at')[:5]





#polls detail view
#Detail of one Polls and vote against it.
class Detail(DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        return Question.objects.filter(published_at__lte=timezone.now())
    


#polls choice list view
#Display after changes of poll choices
class Result(DetailView):
    model = Question
    template_name = "polls/result.html"
    context_object_name = 'question'
    
    
#vote view, to get vote from Detail and incremetn it against the poll and save it.
def vote(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except Exception:
        #choice doesnt' exists or any error
        return render(request,'polls/detail.html', {
            'question': question,
            'error_message':" You didn't select a choice."
        })
    else:
        choice.votes += 1
        choice.save()
    return HttpResponseRedirect(reverse('polls:result',args=(question.id,)))
