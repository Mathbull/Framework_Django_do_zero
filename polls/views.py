from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# define um view baseado em função
def index(request):
    # return HttpResponse('Hello word - index')
    return render(request, 'index.html')


# Define uma view baseado em função.
def ola(request):
    return HttpResponse('index - Hello word')
