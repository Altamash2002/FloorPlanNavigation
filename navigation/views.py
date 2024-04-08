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
    buildings = Building.objects.all()
    floors = Floor.objects.all()
    return render(request, "index.html", {"places": places, "floors": floors, "buildings": buildings, "d_building": d_building, "d_floor": d_floor, "d_place": d_place, "teacher": teacher})


def navigate(request):

    pfrom = request.GET.get('from_place')
    to_place = request.GET.get('to_place')
    from_floor_number = int(request.GET.get('from_floor'))
    to_floor_number = int(request.GET.get('to_floor'))
    current_floor_number = int(request.GET.get('current_floor'))
    fromBuilding = int(request.GET.get('fromBuilding'))
    currentBuilding = int(request.GET.get('currentBuilding'))
    toBuilding = int(request.GET.get('toBuilding'))

    if (currentBuilding == 2) and (currentBuilding == toBuilding):
        if from_floor_number < to_floor_number:
            to = 'c15'
            if current_floor_number != from_floor_number:
                if current_floor_number == to_floor_number:
                    pfrom = 'c16'
                    to = to_place
                else:
                    pfrom = 'c16'
                    to = 'c15'
        elif from_floor_number > to_floor_number:
            to = 'c16'
            if current_floor_number != from_floor_number:
                if current_floor_number == to_floor_number:
                    pfrom = 'c15'
                    to = to_place
                else:
                    pfrom = 'c15'
                    to = 'c16'
        else:
            to = to_place
    elif (currentBuilding == 3) and (currentBuilding == toBuilding):
        if from_floor_number < to_floor_number:
            to = 'c25'
            if current_floor_number != from_floor_number:
                if current_floor_number == to_floor_number:
                    pfrom = 'c26'
                    to = to_place
                else:
                    pfrom = 'c26'
                    to = 'c25'
        elif from_floor_number > to_floor_number:
            to = 'c26'
            if current_floor_number != from_floor_number:
                if current_floor_number == to_floor_number:
                    pfrom = 'c25'
                    to = to_place
                else:
                    pfrom = 'c25'
                    to = 'c26'
        else:
            to = to_place
    elif (currentBuilding == 2) and (currentBuilding != toBuilding):
        if current_floor_number != from_floor_number:
            if (current_floor_number == 0) and (to_floor_number == 0):
                pfrom = 'c15'
                to = to_place
            elif (current_floor_number == 0) and (to_floor_number != 0):
                pfrom = 'c15'
                to = 'c25'
            else:
                pfrom = 'c15'
                to = 'c16'
        else:
            if (current_floor_number == 0) and (to_floor_number == 0):
                to = to_place
            elif (current_floor_number == 0) and (to_floor_number != 0):
                to = 'c25'
            else:
                to = 'c16'
    elif (currentBuilding == 3) and (currentBuilding != toBuilding):
        if current_floor_number != from_floor_number:
            if (current_floor_number == 0) and (to_floor_number == 0):
                pfrom = 'c25'
                to = to_place
            elif (current_floor_number == 0) and (to_floor_number != 0):
                pfrom = 'c25'
                to = 'c15'
            else:
                pfrom = 'c25'
                to = 'c26'
        else:
            if (current_floor_number == 0) and (to_floor_number == 0):
                to = to_place
            elif (current_floor_number == 0) and (to_floor_number != 0):
                to = 'c15'
            else:
                to = 'c26'

    current_floor = get_object_or_404(Floor,floor_no=current_floor_number, building=currentBuilding)
    floor_map = current_floor.svg
    
    destination_floor = get_object_or_404(Floor,floor_no=to_floor_number, building=toBuilding)
    des_place = request.GET.get('to_place')
    des = get_object_or_404(Place,title=des_place,floor_name=destination_floor).name
    
    return render(request , "navigation.html" , {"i": pfrom , "j": to, "floor_map": floor_map, "currentFloor": current_floor, "destinationFloor": destination_floor, "fromBuilding": fromBuilding, "toBuilding": toBuilding, "current_floor_number":current_floor_number, "to_floor_number":to_floor_number,"des":des})

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
