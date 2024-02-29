from django.shortcuts import render,redirect
from .models  import Room,Topic,Message,Profile
from .forms import CreateRoom,Registeruser,UserProfile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    room = Room.objects.all()
    topic = Topic.objects.all()
    message = Message.objects.all()
    context = {'room':room,'topic':topic, 'message':message}
    return render(request,'home.html',context)

def room(request,pk):
    rooms = Room.objects.get(id=pk)
    message = rooms.message_set.all()
    paticipants = rooms.participant.all()
    rooom = rooms.participant.count()
    if request.method == 'POST':
        message1 = Message.objects.create(
            host = request.user,
            body = request.POST.get('message'),
            room = rooms,
        )
        rooms.participant.add(request.user)
        return redirect('room',pk=rooms.id)
    context = {'rooms': rooms, 'message':message,'paticipants':paticipants,'rooom':rooom}
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
        messages.success(request,'Deleted Succesfully')
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
    message = Message.objects.all()

    context = {"topic":topics,"rooms":rooms,'message':message}
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
            messages.success(request,"Your Account Created Succesfully")
            return redirect('home')
    context = {'form':form}
    return render(request,'sign_up.html',context)

def delete_message(request,pk):
    message = Message.objects.get(id=pk)
    if request.method == 'POST':
        message.delete()
        messages.success(request,'Deleted Succesfully')
        return redirect('home')
    return render(request,'delete_room.html',{'obj':message})
    
def search(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        topics = Room.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))

    context = {'search':searched,'topics':topics}
    return render(request,'search.html',context)

def logout_user(request):
    logout(request)
    messages.success(request,'You Succesfully Logout')
    return redirect('home')


def profile(request,pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_message = user.message_set.all()
    topic = Topic.objects.all()
    context = {'user':user,'rooms':rooms,'topic':topic,'room_message':room_message}
    return render(request,'profile.html',context)


@login_required(login_url='login')
def userprofile(request):
    form = UserProfile()
    if request.method == 'POST':
        form = UserProfile(request.POST,request.FILES)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.user = request.user
            forms.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'user_profile.html',context)

@login_required(login_url='login')
def editprofile(request,pk):
    users = Profile.objects.get(id=pk)
    if request.user != request.user:
        messages.error(request,'You arent allowed here')

    user = Profile.objects.get(id=pk)
    form = UserProfile(instance=user)
    if request.method == 'POST':
        form = UserProfile(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'user_profile.html',context)
    

