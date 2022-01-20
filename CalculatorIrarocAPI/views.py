from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Bof, Calculo, Calculoscombinada, Cboregracusteio
from .serializers import BofSerializer, CalculoSerializer, CalculoscombinadaSerializer, CboregracusteioSerializer


class BofAPIView(APIView):
    """API Bof"""
    def get(self, request):
        bof = Bof.objects.all()
        serializer = BofSerializer(bof, many=True)
        return Response(serializer.data)


class CalculoAPIView(APIView):
    """API Calculo"""
    def get (self, request):
        calculo = Calculo.objects.all()
        serializer = CalculoSerializer(calculo, many=True)
        return Response(serializer.data)


class CalculoscombinadaAPIView(APIView):
    """API C.combindas"""
    def get (self, request):
        calculoscombinada = Calculoscombinada.objects.all()
        serializer = CalculoscombinadaSerializer(calculoscombinada, many=True)
        return Response(serializer.data)


class CboregracusteioAPIView(APIView):
    """API cbo r. custeio"""
    def get (self, request):
        cboregracusteio = Cboregracusteio.objects.all()
        serializer = CboregracusteioSerializer(cboregracusteio, many=True)
        return Response(serializer.data)