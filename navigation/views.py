from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Place , Teacher
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(home)  # Redirect to your home page
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(home)  # Redirect to your home page
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})