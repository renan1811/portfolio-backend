from datetime import date

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from core.models import Experiencia, Formacao, Projeto, Tecnologia


class PortfolioAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.tecnologia = Tecnologia.objects.create(
            nome='Django', slug='django', categoria=Tecnologia.Categoria.BACKEND
        )
        self.projeto = Projeto.objects.create(
            titulo='Projeto público', slug='projeto-publico', resumo='Resumo',
            ano=2026, destaque=True, imagem='projetos/capa.png',
        )
        self.projeto.tecnologias.add(self.tecnologia)
        Projeto.objects.create(
            titulo='Rascunho', slug='rascunho', resumo='Não publicar',
            ano=2025, publicado=False,
        )
        Experiencia.objects.create(
            titulo='Experiência pública', organizacao='Organização',
            descricao='Descrição', tipo=Experiencia.Tipo.HACKATHON,
            data_inicio=date(2026, 1, 1),
        )
        Experiencia.objects.create(
            titulo='Experiência privada', organizacao='Organização',
            descricao='Descrição', tipo=Experiencia.Tipo.OUTRA,
            data_inicio=date(2025, 1, 1), publicado=False,
        )
        Formacao.objects.create(
            instituicao='Instituto', curso='Curso público', data_inicio=date(2025, 1, 1)
        )
        Formacao.objects.create(
            instituicao='Instituto', curso='Curso privado',
            data_inicio=date(2024, 1, 1), publicado=False,
        )

    def test_listas_publicas_e_filtro_de_destaque(self):
        for nome, campo, esperado in (
            ('projetos-list', 'titulo', 'Projeto público'),
            ('tecnologias-list', 'nome', 'Django'),
            ('experiencias-list', 'titulo', 'Experiência pública'),
            ('formacoes-list', 'curso', 'Curso público'),
        ):
            with self.subTest(nome=nome):
                resposta = self.client.get(reverse(nome))
                self.assertEqual(resposta.status_code, 200)
                self.assertEqual(len(resposta.data['results']), 1)
                self.assertEqual(resposta.data['results'][0][campo], esperado)

        resposta = self.client.get(reverse('projetos-list'), {'destaque': 'true'})
        self.assertEqual([item['slug'] for item in resposta.data['results']], ['projeto-publico'])
        resposta = self.client.get(reverse('projetos-list'), {'destaque': 'false'})
        self.assertEqual(resposta.data['results'], [])

    def test_detalhe_por_slug_tecnologias_e_url_absoluta_da_imagem(self):
        resposta = self.client.get(reverse('projetos-detail', args=['projeto-publico']))
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.data['tecnologias'][0]['slug'], 'django')
        self.assertEqual(resposta.data['imagem'], 'http://testserver/media/projetos/capa.png')
        self.assertEqual(self.client.get(reverse('projetos-detail', args=['rascunho'])).status_code, 404)

        for recurso, model in (
            ('tecnologias', Tecnologia),
            ('experiencias', Experiencia),
            ('formacoes', Formacao),
        ):
            with self.subTest(recurso=recurso):
                objeto = model.objects.filter(publicado=True).first() if recurso != 'tecnologias' else self.tecnologia
                self.assertEqual(
                    self.client.get(reverse(f'{recurso}-detail', args=[objeto.pk])).status_code,
                    200,
                )

    def test_api_nao_oferece_escrita_anonima(self):
        for recurso, detalhe in (
            ('projetos', 'projeto-publico'),
            ('tecnologias', self.tecnologia.pk),
            ('experiencias', Experiencia.objects.get(publicado=True).pk),
            ('formacoes', Formacao.objects.get(publicado=True).pk),
        ):
            with self.subTest(recurso=recurso):
                lista = reverse(f'{recurso}-list')
                url_detalhe = reverse(f'{recurso}-detail', args=[detalhe])
                for metodo, url in (
                    ('post', lista), ('put', url_detalhe),
                    ('patch', url_detalhe), ('delete', url_detalhe),
                ):
                    resposta = getattr(self.client, metodo)(url, {}, format='json')
                    self.assertEqual(resposta.status_code, 405)
        self.assertEqual(Projeto.objects.count(), 2)
        self.assertTrue(Projeto.objects.get(pk=self.projeto.pk).publicado)


class PortfolioAdminTests(TestCase):
    def test_models_registradas_e_admin_acessivel(self):
        usuario = get_user_model().objects.create_superuser(
            email='admin@example.com', password='senha-de-teste'
        )
        self.client.force_login(usuario)
        for model in (Tecnologia, Projeto, Experiencia, Formacao):
            with self.subTest(model=model.__name__):
                self.assertIn(model, admin.site._registry)
                prefixo = f'admin:core_{model._meta.model_name}'
                self.assertEqual(self.client.get(reverse(f'{prefixo}_changelist')).status_code, 200)
                self.assertEqual(self.client.get(reverse(f'{prefixo}_add')).status_code, 200)

    def test_admin_pode_cadastrar_tecnologia(self):
        usuario = get_user_model().objects.create_superuser(
            email='admin@example.com', password='senha-de-teste'
        )
        self.client.force_login(usuario)
        resposta = self.client.post(
            reverse('admin:core_tecnologia_add'),
            {'nome': 'Vue', 'slug': 'vue', 'icone': '', 'categoria': 'frontend', 'ordem': 0},
        )
        self.assertEqual(resposta.status_code, 302)
        self.assertTrue(Tecnologia.objects.filter(slug='vue').exists())

    def test_admin_pode_cadastrar_projeto_com_tecnologia(self):
        usuario = get_user_model().objects.create_superuser(
            email='admin@example.com', password='senha-de-teste'
        )
        tecnologia = Tecnologia.objects.create(
            nome='Django', slug='django', categoria=Tecnologia.Categoria.BACKEND
        )
        self.client.force_login(usuario)
        resposta = self.client.post(
            reverse('admin:core_projeto_add'),
            {
                'titulo': 'Projeto de teste', 'slug': 'projeto-de-teste',
                'resumo': 'Resumo', 'descricao': '', 'url_github': '', 'url_demo': '',
                'tecnologias': [tecnologia.pk], 'ano': 2026, 'ordem': 0,
                'publicado': 'on',
            },
        )
        self.assertEqual(resposta.status_code, 302)
        projeto = Projeto.objects.get(slug='projeto-de-teste')
        self.assertEqual(list(projeto.tecnologias.all()), [tecnologia])
