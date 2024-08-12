from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, PokemonViewSet, CompetenceViewSet, home

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'pokemons', PokemonViewSet)
router.register(r'competences', CompetenceViewSet)

urlpatterns = [
    path('', home, name='home'),  # Page d'accueil
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
