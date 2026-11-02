from django.db import models

from .tecnologia import Tecnologia


class Projeto(models.Model):
    titulo = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    resumo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='projetos/', blank=True)
    url_github = models.URLField(blank=True)
    url_demo = models.URLField(blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos', blank=True)
    ano = models.PositiveIntegerField()
    destaque = models.BooleanField(default=False)
    publicado = models.BooleanField(default=True)
    ordem = models.PositiveIntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('ordem', '-ano')
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.titulo
