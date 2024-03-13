from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponse
from .models import Place , Teacher, Department, Floor, Building
from .forms import VisitorForm

def detail(request):    
    if not request.session.has_key('login'):
        return redirect(register)
    teachers = Teacher.objects.all()
    departments = Department.objects.all()
    places = Place.objects.all()
    floors = Floor.objects.all()
    buildings = Building.objects.all()
    return render(request, "detail.html", {"teachers":teachers, "departments":departments, "places":places, "floors":floors, "buildings":buildings})

def index(request):
    d_building = None
    d_floor = None
    d_place = None
    if request.method == 'POST':
        teacher_id = request.POST.get('teacher')
        teacher = Teacher.objects.get(id=teacher_id)
        selected_teacher = get_object_or_404(Teacher, id=teacher_id)
        d_place = selected_teacher.place
        d_floor = selected_teacher.floor
        d_building = selected_teacher.building

    places = Place.objects.all()
    floors = Floor.objects.filter(building=d_building)
    return render(request, "index.html", {"places": places, "floors": floors, "d_building": d_building, "d_floor": d_floor, "d_place": d_place, "teacher": teacher})


def navigate(request):

    pfrom = request.GET.get('from_place')
    to_place = request.GET.get('to_place')
    from_floor_id = request.GET.get('from_floor')
    to_floor_id = request.GET.get('to_floor')
    current_floor_id = request.GET.get('current_floor')

    if from_floor_id < to_floor_id:
        to = 'c15'
        if current_floor_id != from_floor_id:
            if current_floor_id == to_floor_id:
                pfrom = 'c16'
                to = to_place
            else:
                pfrom = 'c16'
                to = 'c15'
    elif from_floor_id > to_floor_id:
        to = 'c16'
        if current_floor_id != from_floor_id:
            if current_floor_id == to_floor_id:
                pfrom = 'c15'
                to = to_place
            else:
                pfrom = 'c15'
                to = 'c16'
    else:
        to = to_place

    floor_map = get_object_or_404(Floor,id=from_floor_id).svg
    
    current_floor = get_object_or_404(Floor,id=current_floor_id)
    destination_floor = get_object_or_404(Floor,id=to_floor_id)

    return render(request , "navigation.html" , {"i": pfrom , "j": to, "floor_map": floor_map, "currentFloor": current_floor, "destinationFloor": destination_floor})

def register(request):
    if request.session.has_key('login'):
        return redirect(detail)

    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['login'] = 1
            
            return redirect(detail)
    else:
        form = VisitorForm()

    return render(request, 'register.html', {'form': form})

def home(request):
    return render(request, 'landing.html')
