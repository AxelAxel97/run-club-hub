from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('discussion/', views.discussion, name='discussion'),
    path('login/', views.login, name='login'),
]
