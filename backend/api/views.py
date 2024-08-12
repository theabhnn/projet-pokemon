from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenue sur l'API Pokémon!")

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
