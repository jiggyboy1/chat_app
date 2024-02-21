from django.urls import path
from . import views


urlpatterns =[
    path('',views.home,name="home"),
    path('room/<str:pk>/',views.room,name="room"),
    path('create-room',views.create_room,name="create"),
    path('delete/<str:pk>/',views.delete_room,name="delete"),
    path('delete-message/<str:pk>/',views.delete_message,name="delete_message"),
    path('update/<str:pk>/',views.update,name="update"),
    path('topic/<str:foo>/',views.topic,name="topic"),
    path('login/',views.login_user,name="login"),
    path('sign-up/',views.sign_up,name="register"),
    path('logout/',views.logout_user,name="logout"),
    path('search/',views.search,name="search"),
]