from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm 

# Create your views here.


def home(request):
    q = request.GET.get('q') 
    if q != None:
        q = q
    else:
        q = ''
    topics = Topic.objects.all()
    rooms = Room.objects.filter(topic__name__icontains = q)
    print('rooms:', rooms)
    context = {'salas':rooms, 'topics':topics}
    return render(request, 'home.html', context=context)

def sala(request, pk):
    room = Room.objects.filter(id=pk) 
    context = {'sala': room}        
    return render(request, 'sala.html', context=context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context = {'form': form}
    return render(request, 'room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room) #instance = room nessa linha define que os campos do formulário estarão preenchidos com dados da variável room
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)#instance = room define o model que será alterado 
        if form.is_valid:
            form.save()
            return redirect('homepage')
    context = {'form':form}
    return render(request, 'room_form.html', context)
     
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('homepage')
    context = {'obj': room}
    return render(request, 'delete.html', context )

