from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('discussion/', views.discussion, name='discussion'),
    path('login/', views.login, name='login'),
    path('events/add/', views.add_event, name='add_event'),
    path('events/edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
]
