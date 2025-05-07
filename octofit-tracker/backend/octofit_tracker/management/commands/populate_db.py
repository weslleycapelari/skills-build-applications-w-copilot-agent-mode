from django.core.management.base import BaseCommand
from octofit.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta, date
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Conecta ao MongoDB
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]

        # Remove coleções existentes
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Cria usuários
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='Thunder God', password='thundergodpassword'),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='Metal Geek', password='metalgeekpassword'),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='Zero Cool', password='zerocoolpassword'),
            User(_id=ObjectId(), email='crashoverride@hmhigh.edu', name='Crash Override', password='crashoverridepassword'),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='Sleep Token', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Cria times
        blue_team = Team(_id=ObjectId(), name='Blue Team')
        gold_team = Team(_id=ObjectId(), name='Gold Team')
        blue_team.save()
        gold_team.save()
        for user in users[:3]:
            blue_team.members.add(user)
        for user in users[3:]:
            gold_team.members.add(user)

        # Cria atividades
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Cycling', duration=60, points=30, date=date(2025, 5, 1)),
            Activity(_id=ObjectId(), user=users[1], activity_type='Crossfit', duration=120, points=50, date=date(2025, 5, 2)),
            Activity(_id=ObjectId(), user=users[2], activity_type='Running', duration=90, points=40, date=date(2025, 5, 3)),
            Activity(_id=ObjectId(), user=users[3], activity_type='Strength', duration=30, points=20, date=date(2025, 5, 4)),
            Activity(_id=ObjectId(), user=users[4], activity_type='Swimming', duration=75, points=35, date=date(2025, 5, 5)),
        ]
        Activity.objects.bulk_create(activities)

        # Cria leaderboard
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], points=100, rank=1, week='2025-W18'),
            Leaderboard(_id=ObjectId(), user=users[1], points=90, rank=2, week='2025-W18'),
            Leaderboard(_id=ObjectId(), user=users[2], points=95, rank=3, week='2025-W18'),
            Leaderboard(_id=ObjectId(), user=users[3], points=85, rank=4, week='2025-W18'),
            Leaderboard(_id=ObjectId(), user=users[4], points=80, rank=5, week='2025-W18'),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Cria workouts
        workouts = [
            Workout(_id=ObjectId(), user=users[0], name='Cycling Training', description='Training for a road cycling event', date=date(2025, 5, 1)),
            Workout(_id=ObjectId(), user=users[1], name='Crossfit', description='Training for a crossfit competition', date=date(2025, 5, 2)),
            Workout(_id=ObjectId(), user=users[2], name='Running Training', description='Training for a marathon', date=date(2025, 5, 3)),
            Workout(_id=ObjectId(), user=users[3], name='Strength Training', description='Training for strength', date=date(2025, 5, 4)),
            Workout(_id=ObjectId(), user=users[4], name='Swimming Training', description='Training for a swimming competition', date=date(2025, 5, 5)),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
