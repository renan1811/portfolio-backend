from django.db import models


class Tecnologia(models.Model):
    class Categoria(models.TextChoices):
        FRONTEND = 'frontend', 'Frontend'
        BACKEND = 'backend', 'Backend'
        BANCO_DE_DADOS = 'banco_de_dados', 'Banco de dados'
        FERRAMENTAS = 'ferramentas', 'Ferramentas'
        OUTROS = 'outros', 'Outros'

    nome = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    icone = models.CharField(max_length=100, blank=True)
    categoria = models.CharField(max_length=20, choices=Categoria.choices)
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('ordem', 'nome')
        verbose_name = 'Tecnologia'
        verbose_name_plural = 'Tecnologias'

    def __str__(self):
        return self.nome
