from django.shortcuts import render
from .models import Event


def home(request):
    return render(request, 'club/home.html')


def events(request):
    events = Event.objects.all().order_by('date', 'time')
    return render(request, 'club/events.html', {'events': events})


def discussion(request):
    return render(request, 'club/discussion.html')


def login(request):
    return render(request, 'club/login.html')
