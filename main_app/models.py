from django.db import models
from django.urls import reverse
import datetime  

class MoodEntry(models.Model):
    MOOD_CHOICES = [
        ('Very Happy', 'Very Happy'),
        ('Happy', 'Happy'),
        ('Neutral', 'Neutral'),
        ('Sad', 'Sad'),
    ]

    date = models.DateField(default=datetime.date.today)
    mood = models.CharField(max_length=50, choices=MOOD_CHOICES)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.mood  

    def get_absolute_url(self):
      return reverse('mood-detail', kwargs={'pk': self.id})  

