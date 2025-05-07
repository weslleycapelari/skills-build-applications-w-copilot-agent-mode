from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Team, Activity, Workout, Leaderboard
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class LeaderboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Leaderboard.objects.all().order_by('-points')
    serializer_class = LeaderboardSerializer

@api_view(['GET'])
def api_root(request, format=None):
    codespace_url = 'https://curly-garbanzo-xrgxp7p7rpr2975p-8000.app.github.dev/'
    localhost_url = 'http://localhost:8000/'
    # Retorna ambos os endpoints para facilitar testes locais e via Codespace
    return Response({
        'users': {
            'codespace': codespace_url + 'api/users/?format=api',
            'localhost': localhost_url + 'api/users/?format=api',
        },
        'teams': {
            'codespace': codespace_url + 'api/teams/?format=api',
            'localhost': localhost_url + 'api/teams/?format=api',
        },
        'activities': {
            'codespace': codespace_url + 'api/activities/?format=api',
            'localhost': localhost_url + 'api/activities/?format=api',
        },
        'leaderboard': {
            'codespace': codespace_url + 'api/leaderboard/?format=api',
            'localhost': localhost_url + 'api/leaderboard/?format=api',
        },
        'workouts': {
            'codespace': codespace_url + 'api/workouts/?format=api',
            'localhost': localhost_url + 'api/workouts/?format=api',
        },
    })
