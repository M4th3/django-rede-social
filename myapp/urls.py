from django.urls import path
from .views import home, sala, createRoom, updateRoom, deleteRoom 

urlpatterns = [
    path('', home, name='homepage'),
    path('sala/<str:pk>/', sala, name='sala' ),
    path('create-room/', createRoom, name='create-room'),
    path('update-room/<str:pk>/', updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', deleteRoom, name='delete-room'),
]