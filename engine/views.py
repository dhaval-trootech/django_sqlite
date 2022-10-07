from django.shortcuts import render


# Create your views here.
def my_name(request):
    return render(request, 'engine/engine.html')
