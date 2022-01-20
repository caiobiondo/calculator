from django.urls import path

from .views import BofAPIView, CalculoAPIView, CalculoscombinadaAPIView, CboregracusteioAPIView

urlpatterns = [
    path('bof/', BofAPIView.as_view(), name='bof'),
    path('calculo/', CalculoAPIView.as_view(), name='calculo'),
    path('calculoscombinada/', CalculoscombinadaAPIView.as_view(), name='calculoscombinada'),
    path('cboregracusteio/', CboregracusteioAPIView.as_view(), name='cboregracusteio'),
]