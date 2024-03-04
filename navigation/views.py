from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Place , Teacher

def home(request):
    # place1 = Place(name = 'name1' , floor = 1)
    # teacher = Teacher(name = 'teacher1' , place = 'name1')

    # place1.save()
    # teacher.save()
    places = Place.objects.all()
    return render(request, "index.html", {"places": places})

def navigate(request):

    pfrom = request.GET.get('From')
    to = request.GET.get('To')

    return render(request , "navigation1.html" , {"i": pfrom , "j":to})
