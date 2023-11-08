from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Topic
from .forms import RoomForm 
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def logoutPage(request):
    logout(request)
    return redirect('homepage')

def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            password = User.objects.get(password=password)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) 
            return redirect('homepage')
        else:
            messages.error(request, 'Username or password does not exist')
    
    context={'page' : page}
    return render(request, 'login_register.html', context=context)

def registerPage(request):
    page = 'register'
    context = {'page' : page}
    return render(request, 'login_register.html', context)

def home(request):
    if request.GET.get('q') != None:
        q = request.GET.get('q')
    else:
        q = ''  
    topics = Topic.objects.all()
    rooms = Room.objects.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains = q) |
        Q(description__icontains = q)
    )
    room_count = rooms.count()
    context = {'salas':rooms, 'topics':topics, 'room_count': room_count}
    return render(request, 'home.html', context=context)

@login_required(login_url='/login')
def sala(request, pk):
    room = Room.objects.filter(id=pk) 
    context = {'sala': room}        
    return render(request, 'sala.html', context=context)

@login_required(login_url='/login') 
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context = {'form': form}
    return render(request, 'room_form.html', context)

@login_required(login_url='/login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room) #instance = room nessa linha define que os campos do formulário estarão preenchidos com dados da variável room
    
    if request.user != room.host:
        return HttpResponse('You are not allowed to do this!!!')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)#instance = room define o model que será alterado 
        if form.is_valid:
            form.save()
            return redirect('homepage')
    context = {'form':form}
    return render(request, 'room_form.html', context)
     
@login_required(login_url='/login')     
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('homepage')
    context = {'obj': room}
    return render(request, 'delete.html', context )

