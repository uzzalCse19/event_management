

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count,Q
from .models import Event, Participant, Category,Participant
from .forms import EventForm,CategoryForm,ParticipantForm
from django.utils import timezone

def event_list(request):
    events = Event.objects.select_related('category').prefetch_related('participants').all()
    return render(request, 'event_list.html', {'events': events})
def event_detail(request,pk):
    event=get_object_or_404(Event,pk=pk)
    return render(request,'event_detail.html',{'event':event})

def create_event(request):
    if request.method=='POST':
        form=EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form=EventForm()

    return render(request,'event_form.html',{'form':form})

def update_event(request,pk):
    event=get_object_or_404(Event,pk=pk)
    if request.method=='POST':
        form=EventForm(request.POST,instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form=EventForm(instance=event)

    return render(request,'event_form.html',{'form':form})

def delete_event(request,pk):
    event=get_object_or_404(Event,pk=pk)
    if request.method=='POST':
        event.delete()
        return redirect('event_list')
    else:
        return render(request,'event_confirm_delete.html',{'event':event})


def organizer_dashboard(request):
    current_time = timezone.now()
    total_participants = Participant.objects.count()
    total_events = Event.objects.count()
    upcoming_events = Event.objects.filter(date__gte=current_time).count()
    past_events = Event.objects.filter(date__lt=current_time).count()
    today_events = Event.objects.filter(date=current_time)
    filter_type = request.GET.get('filter')
    data_to_display = None
    if filter_type == 'total_participants':
        data_to_display = Participant.objects.all()
    elif filter_type == 'total_events':
        data_to_display = Event.objects.all()
    elif filter_type == 'upcoming_events':
        data_to_display = Event.objects.filter(date__gte=current_time)
    elif filter_type == 'past_events':
        data_to_display = Event.objects.filter(date__lt=current_time)

   
    return render(request, 'dashboard.html', {
        'total_participants': total_participants,
        'total_events': total_events,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'today_events': today_events,
        'data_to_display': data_to_display,
        'filter_type': filter_type
    })


def search_events(request):
    query = request.GET.get('q', '')  # Ensure query is not None
    events = Event.objects.filter(Q(name__icontains=query) | Q(location__icontains=query)) if query else Event.objects.all()

    return render(request, 'event_list.html', {'events': events, 'query': query})
    
def category_list(request):
    categories=Category.objects.all()
    return render(request,'category_list.html',{'categories':categories})


def create_category(request):
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form=CategoryForm()
    return render(request,'category_form.html',{'form':form})

def update_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    if request.method=='POST':
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid:
            form.save()
            return redirect('category_list')
    else:
        form=CategoryForm(instance=category)
    return render(request,'category_form.html',{'form':form})

def delete_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    if request.method=='POST':
        category.delete()
        return redirect('category_list')
    return render(request,'category_confirm_delete.html',{'category':category})


def participant_list(request):
    participants = Participant.objects.only('id', 'name', 'email').prefetch_related('events')
    return render(request,'participant_list.html',{'participants':participants})

def create_participant(request):
    form=ParticipantForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    return render(request,'participant_form.html',{'form':form})

def update_participant(request,pk):
    partipant=get_object_or_404(Participant.objects.select_related(),pk=pk)
    form=ParticipantForm(request.POST or None,instance=partipant)
    if form.is_valid():
        form.save()
        return redirect('participant_list')
    return render(request,'participant_form.html',{'form':form})

def delete_participant(request,pk):
    participant=get_object_or_404(Participant.objects.only('id'),pk=pk)
    if request.method=='POST':
        participant.delete()
        return redirect('participant_list')
    return render(request,'participant_confirm_delete.html',{'participant':participant})





