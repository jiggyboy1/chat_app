from django.urls import path
from . import views


urlpatterns =[
    path('',views.home,name="home"),
    path('room/<str:pk>/',views.room,name="room"),
    path('create-room',views.create_room,name="create"),
    path('delete/<str:pk>/',views.delete_room,name="delete"),
    path('update/<str:pk>/',views.update,name="update"),
    path('topic/<str:foo>/',views.topic,name="topic"),
]