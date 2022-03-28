
from django.shortcuts import redirect, render

from .models import Todo


# Create your views here.
def index(request):
    todo = Todo.objects.all()
    if request.method == 'POST':
        new_Todo = Todo (
            title = request.POST['title'],
        )
        new_Todo.save()
        return redirect('/')

    return render(request, 'index.html', {'todo': todo})


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('/')

