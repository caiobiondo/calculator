from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Bof, Calculo, Calculoscombinada, Cboregracusteio, Comboloan, Dadoscalculadorapipeline, \
    Dgabaseoperacoes, Dgaceadiario, Dgacurvasjuros, Dgagrupos, Dgamatrizmigracao, Dgamontecarlo, \
    Dgaparametrosestrategiaportfolio, Dgapercentualfepf, Dgarcpalfasbetas, Dgatargetpais, Fprcnpj, Garantiabem, Garantia
from .serializers import BofSerializer, CalculoSerializer, CalculoscombinadaSerializer, CboregracusteioSerializer, \
    ComboloanSerializer, DadoscalculadorapipelineSerializer, DgabaseoperacoesSerializer, DgaceadiarioSerializer, \
    DgacurvasjurosSerializer, DgagruposSerializer, DgamatrizmigracaoSerializer, DgamontecarloSerializer, \
    DgaparametrosestrategiaportfolioSerializer, DgapercentualfepfSerializer, DgarcpalfasbetasSerializer, \
    DgatargetpaisSerializer, FprcnpjSerializer, GarantiabemSerializer, GarantiaSerializer


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


class ComboloanAPIView(APIView):
    """API ComboLoan"""
    def get (self, request):
        comboloan = Comboloan.objects.all()
        serializer = ComboloanSerializer(comboloan, many=True)
        return Response(serializer.data)


class DadoscalculadorapipelineAPIView(APIView):
    """API calc"""
    def get (self, request):
        dadoscalculadorapipeline = Dadoscalculadorapipeline.objects.all()
        serializer = DadoscalculadorapipelineSerializer(dadoscalculadorapipeline, many=True)
        return Response(serializer.data)


class DgabaseoperacoesAPIView(APIView):
    """...."""
    def get (self, request):
        dgabaseoperacoes = Dgabaseoperacoes.objects.all()
        serializer = DgabaseoperacoesSerializer(dgabaseoperacoes, many=True)
        return Response(serializer.data)


class DgaceadiarioAPIView(APIView):
    """...."""
    def get (self, request):
        dgaceadiario = Dgaceadiario.objects.all()
        serializer = DgaceadiarioSerializer(dgaceadiario, many=True)
        return Response(serializer.data)


class DgacurvasjurosAPIView(APIView):
    """....."""
    def get (self, request):
        dgacurvasjuros = Dgacurvasjuros.objects.all()
        serializer = DgacurvasjurosSerializer(dgacurvasjuros, many=True)
        return Response(serializer.data)


class DgagruposAPIView(APIView):
    """...."""
    def get (self, request):
        dgagrupos = Dgagrupos.objects.all()
        serializer = DgagruposSerializer(dgagrupos, many=True)
        return Response(serializer.data)


class DgamatrizmigracaoAPIView(APIView):
    """...."""
    def get (self, request):
        dgamatrizmigracao = Dgamatrizmigracao.objects.all()
        serializer = DgamatrizmigracaoSerializer(dgamatrizmigracao, many=True)
        return Response(serializer.data)


class DgamontecarloAPIView(APIView):
    """...."""
    def get (self, request):
        dgamontecarlo = Dgamontecarlo.objects.all()
        serializer = DgamontecarloSerializer(dgamontecarlo, many=True)
        return Response(serializer.data)


class DgaparametrosestrategiaportfolioAPIView(APIView):
    """...."""
    def get (self, request):
        dgaparametrosestrategiaportfolio = Dgaparametrosestrategiaportfolio.objects.all()
        serializer = DgaparametrosestrategiaportfolioSerializer(dgaparametrosestrategiaportfolio, many=True)
        return Response(serializer.data)


class DgapercentualfepfAPIView(APIView):
    """...."""
    def get (self, request):
        dgapercentualfepf = Dgapercentualfepf.objects.all()
        serializer = DgapercentualfepfSerializer(dgapercentualfepf, many=True)
        return Response(serializer.data)


class DgarcpalfasbetasAPIView(APIView):
    """...."""
    def get (self, request):
        dgarcpalfasbetas = Dgarcpalfasbetas.objects.all()
        serializer = DgarcpalfasbetasSerializer(dgarcpalfasbetas, many=True)
        return Response(serializer.data)


class DgatargetpaisAPIView(APIView):
    """...."""
    def get (self, request):
        dgatargetpais = Dgatargetpais.objects.all()
        serializer = DgatargetpaisSerializer(dgatargetpais, many=True)
        return Response(serializer.data)


class FprcnpjAPIView(APIView):
    """...."""
    def get (self, request):
        fprcnpj = Fprcnpj.objects.all()
        serializer = FprcnpjSerializer(fprcnpj, many=True)
        return Response(serializer.data)


class GarantiabemAPIView(APIView):
    """...."""
    def get (self, request):
        garantiabem = Garantiabem.objects.all()
        serializer = GarantiabemSerializer(garantiabem, many=True)
        return Response(serializer.data)


class GarantiaAPIView(APIView):
    """...."""
    def get (self, request):
        garantia = Garantia.objects.all()
        serializer = GarantiaSerializer(garantia, many=True)
        return Response(serializer.data)

