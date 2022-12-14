# Generated by Django 3.0.7 on 2022-11-23 17:42

from django.db import migrations, models
import django.db.models.deletion
import f1.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('campeonatoID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('pilotosRegulamentoOriginal', models.ImageField(blank=True, null=True, upload_to=f1.models.upload_image_campeonato)),
                ('pilotosRegulamentoDe2022', models.ImageField(blank=True, null=True, upload_to=f1.models.upload_image_campeonato)),
                ('pilotosRegulamentoVoltaMaisR√°pidaPole', models.ImageField(blank=True, null=True, upload_to=f1.models.upload_image_campeonato)),
                ('pilotosRegulamentoDecrescimo', models.ImageField(blank=True, null=True, upload_to=f1.models.upload_image_campeonato)),
                ('resultadoEquipes', models.ImageField(blank=True, null=True, upload_to=f1.models.upload_image_campeonato)),
            ],
        ),
        migrations.CreateModel(
            name='DadosCampeonato',
            fields=[
                ('dadosID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f1.Campeonato')),
            ],
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('equipeID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nomeEquipe', models.CharField(max_length=30)),
                ('posicaoEquipe', models.IntegerField(null=True)),
                ('pontuacao_equipe', models.FloatField(null=True)),
                ('imagemEquipe', models.ImageField(blank=True, null=True, upload_to=f1.models.upload_image_equipe)),
            ],
        ),
        migrations.CreateModel(
            name='Piloto',
            fields=[
                ('pilotoID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nomePiloto', models.CharField(max_length=30)),
                ('posicaoPiloto', models.CharField(max_length=10)),
                ('pontuacaoPiloto', models.CharField(max_length=10)),
                ('descricao', models.CharField(max_length=10000)),
                ('distribuicaoFrequencias', models.ImageField(blank=True, null=True, upload_to=f1.models.upload_image_piloto)),
                ('graficoFrequencias', models.ImageField(blank=True, null=True, upload_to=f1.models.upload_image_piloto)),
                ('graficoPorcentagem', models.ImageField(blank=True, null=True, upload_to=f1.models.upload_image_piloto)),
                ('piePlot', models.ImageField(blank=True, null=True, upload_to=f1.models.upload_image_piloto)),
                ('imagemPiloto', models.ImageField(blank=True, null=True, upload_to=f1.models.upload_image_piloto)),
            ],
        ),
        migrations.CreateModel(
            name='Temporada',
            fields=[
                ('temporadaID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('temporada', models.CharField(max_length=30)),
                ('dadosCampeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f1.DadosCampeonato')),
            ],
        ),
        migrations.AddField(
            model_name='dadoscampeonato',
            name='equipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f1.Equipe'),
        ),
        migrations.AddField(
            model_name='dadoscampeonato',
            name='piloto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='f1.Piloto'),
        ),
    ]
