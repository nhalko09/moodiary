from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import MoodEntry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def mood_index(request):
    entries = MoodEntry.objects.all().order_by('-date')
    return render(request, 'moods/index.html', {'entries': entries})

def mood_detail(request, pk):
    entry = MoodEntry.objects.get(id=pk)
    return render(request, 'moods/detail.html', {'entry': entry})

class MoodCreate(LoginRequiredMixin, CreateView):
    model = MoodEntry
    fields = '__all__'
    template_name = 'main_app/mood-form.html'


class MoodUpdate(UpdateView):
    model = MoodEntry
    fields = ['date', 'mood', 'notes']
    template_name = 'main_app/mood-form.html'


class MoodDelete(DeleteView):
    model = MoodEntry
    template_name = 'main_app/mood_confirm_delete.html' 
    success_url = '/moods/'

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'