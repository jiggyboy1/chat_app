from django.shortcuts import render
from .models  import Room,Topic

# Create your views here.

def home(request):
    room = Room.objects.all()
    context = {'room':room}
    return render(request,'home.html',context)