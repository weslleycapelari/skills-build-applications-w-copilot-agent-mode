from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@example.com', name='Test User', password='123456')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(email='team@example.com', name='Team User', password='123456')
        team = Team.objects.create(name='Team A')
        team.members.add(user)
        self.assertEqual(team.name, 'Team A')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email='activity@example.com', name='Activity User', password='123456')
        activity = Activity.objects.create(user=user, activity_type='run', duration=30, points=10, date=timezone.now())
        self.assertEqual(activity.activity_type, 'run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(email='workout@example.com', name='Workout User', password='123456')
        workout = Workout.objects.create(user=user, name='Morning Run', description='5km run', date=timezone.now())
        self.assertEqual(workout.name, 'Morning Run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create(email='leader@example.com', name='Leader User', password='123456')
        leaderboard = Leaderboard.objects.create(user=user, points=100, rank=1, week='2025-W19')
        self.assertEqual(leaderboard.rank, 1)
