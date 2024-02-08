from django.shortcuts import render,redirect
from .models  import Room,Topic
from .forms import CreateRoom

# Create your views here.

def home(request):
    room = Room.objects.all()
    topic = Topic.objects.all()
    context = {'room':room,'topic':topic}
    return render(request,'home.html',context)

def room(request,pk):
    rooms = Room.objects.get(id=pk)
    context = {'rooms': rooms}
    return render(request,'room_page.html',context)

def create_room(request):
    form = CreateRoom()
    if request.method == 'POST':
        form = CreateRoom(request.POST)
        if form.is_valid():
            forms =form.save(commit=False)
            forms.host = request.user
            forms.save()

    context = {'form':form}
    return render(request,'create.html',context)

def delete_room(request,pk):
    room_delete = Room.objects.get(id=pk)
    if request.method == 'POST':
        room_delete.delete()
        return redirect('home')
    return render(request,'delete_room.html',{'obj':room_delete})

def update(request,pk):
    room = Room.objects.get(id=pk)
    form = CreateRoom(instance=room)
    if request.method == 'POST':
        form = CreateRoom(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'create.html',context)

def topic(request,foo):
    topics = Topic.objects.get(name=foo)
    rooms = Room.objects.filter(topic=topics)

    context = {"topic":topics,"rooms":rooms}
    return render(request,'topic.html',context)