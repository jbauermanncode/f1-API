from rest_framework import serializers
from f1.models import Equipe, Piloto, Campeonato, DadosCampeonato, Temporada

class PilotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto
        fields = '__all__'

class EquipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = '__all__'

class CampeonatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campeonato
        fields = '__all__'

class DadosCampeonatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosCampeonato
        fields = '__all__'
        exclude = []

class ListaPilotosEmUmCampeonatoSerializer(serializers.ModelSerializer):
    piloto_nome = serializers.ReadOnlyField(source='pilotos.nomePiloto')
    class Meta:
        model = DadosCampeonato
        fields = ['piloto']

class ListaEquipesEmUmCampeonatoSerializer(serializers.ModelSerializer):
    piloto_nome = serializers.ReadOnlyField(source='equipes.nomeEquipe')
    class Meta:
        model = DadosCampeonato
        fields = ['equipe']

class TemporadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporada
        fields = '__all__'
        exclude = []