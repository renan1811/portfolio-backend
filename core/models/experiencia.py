from django.db import models


class Experiencia(models.Model):
    class Tipo(models.TextChoices):
        PROFISSIONAL = 'profissional', 'Experiência profissional'
        HACKATHON = 'hackathon', 'Hackathon'
        OUTRA = 'outra', 'Outra experiência'

    titulo = models.CharField(max_length=150)
    organizacao = models.CharField(max_length=150)
    descricao = models.TextField()
    tipo = models.CharField(max_length=20, choices=Tipo.choices)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    atual = models.BooleanField(default=False)
    ordem = models.PositiveIntegerField(default=0)
    publicado = models.BooleanField(default=True)

    class Meta:
        ordering = ('ordem', '-data_inicio')
        verbose_name = 'Experiência'
        verbose_name_plural = 'Experiências'

    def __str__(self):
        return f'{self.titulo} — {self.organizacao}'
