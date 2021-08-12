from django.shortcuts import render, get_object_or_404, redirect
from .forms import dive
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = dive(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('login')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'users/register.html', context)
    else :
        form = dive()
        return render(request, 'users/register.html', {'form':form})
    