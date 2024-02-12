from django.shortcuts import render,redirect
from .models  import Room,Topic
from .forms import CreateRoom,Registeruser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


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

@login_required(login_url='login')
def create_room(request):
    form = CreateRoom()
    if request.method == 'POST':
        form = CreateRoom(request.POST)
        if form.is_valid():
            forms =form.save(commit=False)
            forms.host = request.user
            forms.save()
            return redirect('home')

    context = {'form':form}
    return render(request,'create.html',context)

def delete_room(request,pk):
    room_delete = Room.objects.get(id=pk)
    if request.method == 'POST':
        room_delete.delete()
        return redirect('home')
    return render(request,'delete_room.html',{'obj':room_delete})

@login_required(login_url='login')
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

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')

    context = {}
    return render(request,'login.html',context)

def sign_up(request):
    form = Registeruser()
    if request.method == 'POST':
        form = Registeruser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    context = {'form':form}
    return render(request,'sign_up.html',context)


def logout_user(request):
    logout(request)
    return redirect('home')