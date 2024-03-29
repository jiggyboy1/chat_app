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
    participant= models.ManyToManyField(User,related_name='paticipants',blank=True)
    description = models.TextField(max_length=600,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return f'{self.description[0:70]}'

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='image/',blank=True,null=True)
    bio = models.CharField(blank=True,null=True,max_length=200)
    location = models.CharField(blank=True,null=True,max_length=200)
    zip_code = models.CharField(blank=True,null=True,max_length=200)

    def __str__(self) -> str:
        return f'{self.user.username}'

    
class Message(models.Model):
    host = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    body = models.TextField(max_length=200,null=True,blank=True)
    created = models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ['-created']

        
    def __str__(self) -> str:
        return f'{self.body}'