from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponse
from .models import Place , Teacher

def detail(request):
    teachers = Teacher.objects.all()
    return render(request, "detail.html", {"teachers":teachers})

def home(request):
    if request.method == 'POST':
        teacher = request.POST.get('teacher')
        destination = get_object_or_404(Teacher, name=teacher).place
    places = Place.objects.all()
    return render(request, "index.html", {"places": places, "destination": destination})

def navigate(request):

    pfrom = request.GET.get('From')
    to = request.GET.get('To')

    return render(request , "navigation.html" , {"i": pfrom , "j":to})
