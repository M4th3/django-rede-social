from django.urls import path
from .views import home, sala, createRoom, updateRoom, deleteRoom, loginPage, logoutPage, registerPage

urlpatterns = [
    path('logout/', logoutPage, name='logout'),
    path('login/', loginPage, name='login'),
    path('', home, name='homepage'),
    path('sala/<str:pk>/', sala, name='sala' ),
    path('create-room/', createRoom, name='create-room'),
    path('update-room/<str:pk>/', updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', deleteRoom, name='delete-room'),
    path('register/', registerPage, name='register'),
]