from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"

class Room(models.Model):
    name = models.CharField(max_length=100,)
    host = models.ForeignKey(User,on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    # participant=
    description = models.TextField(max_length=200,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name} {self.topic}'
    
class Message(models.Model):
    host = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    body = models.TextField(max_length=200,null=True,blank=True)
    created = models.DateTimeField(auto_now_add= True)

    def __str__(self) -> str:
        return f'{self.body}'