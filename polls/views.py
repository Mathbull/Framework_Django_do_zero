from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from polls.models import Question

# define um view baseado em função
def index(request):
    # return HttpResponse('Hello word - index')
    # return render(request, 'index.html')
    
    return render(request, 'index.html', {'titulo': 'Últimas enquetes',})


# Define uma view baseado em função.
def ola(request):
    # return HttpResponse('index - Hello word')
    question = Question.objects.all()
    context = {'all_question': question}
    return render(request, 'polls/question.html', context)
    
    
