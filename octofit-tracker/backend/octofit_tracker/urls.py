"""
URL configuration for octofit_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from octofit import views

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'teams': reverse('team-list', request=request, format=format),
        'activities': reverse('activity-list', request=request, format=format),
        'workouts': reverse('workout-list', request=request, format=format),
        'leaderboard': reverse('leaderboard-list', request=request, format=format),
    })

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', api_root, name='api-root'),
    path('users/', views.UserListCreateView.as_view(), name='user-list'),
    path('users/<str:pk>/', views.UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('teams/', views.TeamListCreateView.as_view(), name='team-list'),
    path('teams/<str:pk>/', views.TeamRetrieveUpdateDestroyView.as_view(), name='team-detail'),
    path('activities/', views.ActivityListCreateView.as_view(), name='activity-list'),
    path('activities/<str:pk>/', views.ActivityRetrieveUpdateDestroyView.as_view(), name='activity-detail'),
    path('workouts/', views.WorkoutListCreateView.as_view(), name='workout-list'),
    path('workouts/<str:pk>/', views.WorkoutRetrieveUpdateDestroyView.as_view(), name='workout-detail'),
    path('leaderboard/', views.LeaderboardListView.as_view(), name='leaderboard-list'),
]
