from django.shortcuts import render,HttpResponse
from .forms import ToDO

# Create your views here.
def Intro(request):
    return HttpResponse ("<h1>Hello World</h1>")

def todo(request):
    return HttpResponse ('<h1> App is Under Construction</h1>')

def todoForm(request):
    form = ToDO()
    context = {'form': form}
    return render (request, 'to_do_app/todo.html',context)
