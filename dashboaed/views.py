from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
# HOME PAGE
def homepage(request):
    events = Event.objects.all()  # Get all events
    return render(request, 'index.html', {'events': events})

@login_required
def dashboard(request):
    # Get the user's profile
    user_profile = request.user.userprofile  # Assuming you've set up a OneToOne relationship
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'accounts/dashboard.html', context=context)
# AdminDashboard
@login_required(login_url='login')
def admin_view(request):
    events = Event.objects.all()  # Fetch all events
    context = {
        'events': events
    }
    return render(request, 'admindashboard/admin_dashboard.html', context)


# Event creation
@login_required
def create_event(request):
    if request.method == 'POST':
        # Extract form data from request.POST
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        poster = request.FILES.get('poster')  # Handle file upload

        # Basic validation
        if not title or not description or not date or not time or not location:
            messages.error(request, "All fields are required.")
            return render(request, 'admindashboard/event_creation.html')

        # Create a new event instance and save it
        event = Event(
            title=title,
            description=description,
            date=date,
            time=time,
            location=location,
            poster=poster
        )
        event.user = request.user  # Associate the event with the logged-in user
        event.save()  # Save the event to the database

        # Show success message
        messages.success(request, "Event created successfully!")
        # Redirect to the event dashboard after creation
        return redirect('dashboard')

    return render(request, 'admindashboard/event_creation.html')  # Render the event creation template if not POST

# Editing event
@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.title = request.POST.get('title')
        event.description = request.POST.get('description')
        event.date = request.POST.get('date')
        event.time = request.POST.get('time')
        event.location = request.POST.get('location')
        
        # Handle poster upload if provided
        if request.FILES.get('poster'):
            event.poster = request.FILES.get('poster')
        
        event.save()
        return redirect('dashboard')  # Redirect to the dashboard after editing

    return render(request, 'admindashboard/edit_event.html', {'event': event})

# Deleting event
@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        event.delete()
        return redirect('dashboard')  # Redirect after deletion

    return render(request, 'admindashboard/delete.html', {'event': event})