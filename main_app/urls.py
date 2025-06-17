from django.urls import path
from . import views 
from .views import SignupView
from django.contrib.auth import views as auth_views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('moods/', views.mood_index, name='mood-index'),
    path('moods/<int:pk>/', views.mood_detail, name='mood-detail'),
    path('moods/create/', views.MoodCreate.as_view(), name='mood-create'),
    path('moods/<int:pk>/update/', views.MoodUpdate.as_view(), name='mood-update'),
    path('moods/<int:pk>/delete/', views.MoodDelete.as_view(), name='mood-delete'),
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(
    redirect_authenticated_user=True,
    next_page='/'
    ), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),


]