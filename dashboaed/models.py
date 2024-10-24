from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields you want to store for each user
    bio = models.TextField(blank=True)
    # Add more fields as necessary

    def __str__(self):
        return self.user.username
    
    
    
    
    
# Event Creation
class Event(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who created the event
    title = models.CharField(max_length=100)                       # Title of the event
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)  # Image field for event poster
    description = models.TextField()                                # Description of the event
    date = models.DateField()                                      # Date of the event
    time = models.TimeField()                                      # Time of the event
    location = models.CharField(max_length=200)                   # Location of the event
    created_at = models.DateTimeField(auto_now_add=True)          # Timestamp when the event is created
    
    def __str__(self):
        return self.title  # String representation of the event