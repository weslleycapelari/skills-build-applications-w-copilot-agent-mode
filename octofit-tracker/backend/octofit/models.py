from django.db import models
from djongo import models as djongo_models

class User(djongo_models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True, editable=False)
    email = djongo_models.EmailField(unique=True)
    name = djongo_models.CharField(max_length=100)
    password = djongo_models.CharField(max_length=128)
    created_at = djongo_models.DateTimeField(auto_now_add=True)
    updated_at = djongo_models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class Team(djongo_models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True, editable=False)
    name = djongo_models.CharField(max_length=100, unique=True)
    members = djongo_models.ArrayReferenceField(to=User)
    created_at = djongo_models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Activity(djongo_models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True, editable=False)
    user = djongo_models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = djongo_models.CharField(max_length=50)
    duration = djongo_models.IntegerField()  # minutos
    distance = djongo_models.FloatField(null=True, blank=True)  # km
    points = djongo_models.IntegerField(default=0)
    date = djongo_models.DateField()
    created_at = djongo_models.DateTimeField(auto_now_add=True)

class Workout(djongo_models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True, editable=False)
    user = djongo_models.ForeignKey(User, on_delete=models.CASCADE)
    name = djongo_models.CharField(max_length=100)
    description = djongo_models.TextField()
    date = djongo_models.DateField()
    created_at = djongo_models.DateTimeField(auto_now_add=True)

class Leaderboard(djongo_models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True, editable=False)
    user = djongo_models.ForeignKey(User, on_delete=models.CASCADE)
    points = djongo_models.IntegerField(default=0)
    rank = djongo_models.IntegerField(default=0)
    week = djongo_models.CharField(max_length=20)
    created_at = djongo_models.DateTimeField(auto_now_add=True)
