from django.shortcuts import render,HttpResponse
from .forms import ToDO

# Create your views here.
def Intro(request):
    return render(request, 'to_do_app/home.html')

def todo(request):
    return HttpResponse ('<h1> App is Under Construction</h1>')

def todoForm(request):
    form = ToDO()
    context = {'form': form}
    if request.method == 'POST':
        form = ToDO(request.POST)
        if form.is_valid():
            todo = form.cleaned_data.get('todo')
            return render(request, 'to_do_app/sample.html',{'data':todo})
    return render (request, 'to_do_app/todo.html',context)
