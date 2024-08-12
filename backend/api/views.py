from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import User, Pokemon, Competence
from .serializers import UserSerializer, PokemonSerializer, CompetenceSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class CompetenceViewSet(viewsets.ModelViewSet):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer
