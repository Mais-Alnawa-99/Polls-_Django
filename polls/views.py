from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render 
from django.urls import reverse
from .models import Questions ,Choice

def index (request):
  question_list= Questions.objects.order_by("-pup_date")
  return render (request ,'index.html' ,{"question_list": question_list})
 
def detail (request,question_id):
     question=get_object_or_404(Questions,pk=question_id)
     return render ( request, 'detail.html',{"question": question} ) 
def result (request,question_id):
     question=get_object_or_404(Questions,pk=question_id)
     return render ( request, 'result.html',{"question": question} ) 
def vote (request,question_id):
   question = get_object_or_404(Questions, pk=question_id)
   try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
   except (KeyError, Choice.DoesNotExist):
        
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
   else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('result',args=(question.id,)))
       
 

       