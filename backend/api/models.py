from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    team_pokemons = models.ManyToManyField('Pokemon', blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='api_users',  # Ajout d'un related_name unique
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='api_user_permissions',  # Ajout d'un related_name unique
        blank=True,
    )

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    hp = models.IntegerField()

class Competence(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    damage = models.IntegerField()
    accuracy = models.FloatField()