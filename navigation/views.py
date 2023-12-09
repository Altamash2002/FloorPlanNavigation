from django.shortcuts import render
from django.http import HttpResponse
from .models import Place , Teacher

# Create your views here.

def home(request):
    # place1 = Place(name = 'name1' , floor = 1)
    # teacher = Teacher(name = 'teacher1' , place = 'name1')

    # place1.save()
    # teacher.save()
    places = Place.objects.all()
    return render(request, "index.html", {"places": places})

def navigate(request):

    room = request.GET.get('To')

    return render(request , "navigation.html" , {"destination": room})