from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Bof(Base):
    segmento = models.CharField(max_length=255)
    produto = models.CharField(max_length=255)
    modalidade = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Bof'
        verbose_name_plural = 'Bofs'

    def __str__(self):
        return self.segmento


class Calculo(Base):
    calculo = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Calculo'
        verbose_name_plural = 'Calculos'

    def __str__(self):
        return f'{self.calculo}'


class Calculoscombinada(Base):
    ids_calc = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Calculoscombinada'
        verbose_name_plural = 'Calculoscombinadas'

        def __str__(self):
            return f'{self.ids_calc}'


class Cboregracusteio(Base):
    produto = models.ForeignKey(Bof, related_name='produtos', on_delete=models.CASCADE)
    modalidade = models.ForeignKey(Bof, related_name='modalidades',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cboregracusteio'
        verbose_name_plural = 'Cboregracusteios'

    def __str__(self):
        return f'{self.produto} / {self.modalidade}'
