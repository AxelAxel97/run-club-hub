from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm


def home(request):
    return render(request, 'club/home.html')


def events(request):
    events = Event.objects.all().order_by('date', 'time')
    return render(request, 'club/events.html', {'events': events})


def discussion(request):
    return render(request, 'club/discussion.html')


def login(request):
    return render(request, 'club/login.html')


def add_event(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('events')
    return render(request, 'club/add_event.html', {'form': form})


def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('events')
    return render(request, 'club/edit_event.html', {'form': form, 'event': event})


def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('events')
    return render(request, 'club/delete_event.html', {'event': event})
