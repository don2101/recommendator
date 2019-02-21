from django.shortcuts import render, redirect
from .models import Question, Choice

# Create your views here.

def main(request) :
    context = {}
    options = Choice.objects.filter(question_id=1).all()
    
    context['options'] = options
    
    return render(request, 'recommendation/main.html', context)
    
def select(request) :
    menu = request.GET.get('menu')

    choice = Choice.objects.get(content=menu)
    choice.votes = choice.votes + 1
    
    choice.save()
    
    return redirect('main')