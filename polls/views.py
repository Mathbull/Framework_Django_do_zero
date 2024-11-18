from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.http import HttpResponse


from polls.models import Question
from polls.forms import QuestionForm

# define um view baseado em função
def index(request):
    # return HttpResponse('Hello word - index')
    # return render(request, 'index.html')
    aviso = 'aviso importante: esstá pagina não exige login....'
    messages.warning(request, aviso)
    return render(request, 'index.html', {'titulo': 'Últimas enquetes',})


# Define uma view baseado em função.
@login_required
def ola(request):
    # return HttpResponse('index - Hello word')
    question = Question.objects.all()
    context = {'all_question': question}
    return render(request, 'polls/question.html', context)


class QuestionCreateView(LoginRequiredMixin,CreateView):
    model = Question
    template_name = "polls/question_form.html"
    fields = ("question_text", "pub_date")
    success_url = reverse_lazy("index")
    success_message = "Pergunta criada com sucesso..."

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(QuestionCreateView, self).form_valid(form)    

@login_required
def question_create(request):
    context = {}
    form = QuestionForm(request.POST or None, request.FILES or None)
    context['form'] =form

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Pergunta criada com sucesso!')
            return redirect('index')
    return render(request, 'polls/question_form.html', context)