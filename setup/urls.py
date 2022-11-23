from django.urls import path, include
from django.contrib import admin
from f1.views import EquipeViewSet, PilotoViewSet, CampeonatoViewSet, DadosCampeonatoViewSet, ListaPilotosEmUmCampeonato, ListaEquipesEmUmCampeonato, TemporadaViewSet
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('pilotos', PilotoViewSet, basename = 'Pilotos')
router.register('equipes', EquipeViewSet, basename = 'Equipes')
router.register('campeonatosPilotos', CampeonatoViewSet, basename = 'Campeonato')
router.register('dadosPilotos', DadosCampeonatoViewSet, basename = 'DadosPilotos')
router.register('dadosEquipes', DadosCampeonatoViewSet, basename = 'DadosEquipes')
router.register('temporadas', TemporadaViewSet, basename = 'Temporadas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('campeonatosPilotos/<int:pk>/dadosPilotos/', ListaPilotosEmUmCampeonato.as_view()),
    path('campeonatosEquipes/<int:pk>/dadosEquipes/', ListaEquipesEmUmCampeonato.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


