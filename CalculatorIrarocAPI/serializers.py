from rest_framework import serializers

from .models import Bof, Calculo, Calculoscombinada, Cboregracusteio


class BofSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bof
        fields = (
            'id',
            'segmento',
            'produto',
            'modalidade',
             'criacao',
            'ativo'
        )


class CalculoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calculo
        fields = (
            'id',
            'calculo'
        )


class CalculoscombinadaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calculoscombinada
        fields = (
            'id',
            'ids_calc'
        )


class CboregracusteioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cboregracusteio
        fields = (
            'produto',
            'modalidade'
        )
