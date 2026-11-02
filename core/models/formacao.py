from django.db import models


class Formacao(models.Model):
    instituicao = models.CharField(max_length=150)
    curso = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    em_andamento = models.BooleanField(default=False)
    ordem = models.PositiveIntegerField(default=0)
    publicado = models.BooleanField(default=True)

    class Meta:
        ordering = ('ordem',)
        verbose_name = 'Formação'
        verbose_name_plural = 'Formações'

    def __str__(self):
        return f'{self.curso} — {self.instituicao}'
