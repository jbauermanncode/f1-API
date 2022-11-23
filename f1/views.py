from rest_framework import viewsets, generics
from f1.models import Equipe, Piloto, Campeonato, DadosCampeonato, Temporada
from f1.serializer import EquipesSerializer, PilotosSerializer, CampeonatosSerializer, DadosCampeonatosSerializer, ListaPilotosEmUmCampeonatoSerializer, ListaEquipesEmUmCampeonatoSerializer, TemporadasSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class PilotoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os pilotos"""
    queryset = Piloto.objects.all()
    serializer_class = PilotosSerializer
    authentication_classes = [BasicAuthentication]
    permissions_classes = [IsAuthenticated]

class EquipeViewSet(viewsets.ModelViewSet):
    """Exibindo todas as equipes"""
    queryset = Equipe.objects.all()
    serializer_class = EquipesSerializer

class CampeonatoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os campeonatos"""
    queryset = Campeonato.objects.all()
    serializer_class = CampeonatosSerializer

class DadosCampeonatoViewSet(viewsets.ModelViewSet):
    """Listando dados dos pilotos"""
    queryset = DadosCampeonato.objects.all()
    serializer_class = DadosCampeonatosSerializer

class ListaPilotosEmUmCampeonato(generics.ListAPIView):
    """Lista pilotos em um campeonato"""
    def get_queryset(self):
        queryset = DadosCampeonato.objects.filter(campeonatoPilotosID=self.kwargs['pk'])
        return queryset
    serializer_class = ListaPilotosEmUmCampeonatoSerializer

class ListaEquipesEmUmCampeonato(generics.ListAPIView):
    """Lista equipes em um campeonato"""
    def get_queryset(self):
        queryset = DadosCampeonato.objects.filter(campeonatoPilotosID=self.kwargs['pk'])
        return queryset
    serializer_class = ListaEquipesEmUmCampeonatoSerializer

class TemporadaViewSet(viewsets.ModelViewSet):
    """Listando temporadas"""
    queryset = Temporada.objects.all()
    serializer_class = TemporadasSerializer

