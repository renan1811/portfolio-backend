# Portfolio Backend

API Django REST Framework baseada na estrutura do [template Django/PDM de Marco André](https://github.com/marrcandre/template_django_pdm) e no [tutorial Django/DRF](https://github.com/marrcandre/django-drf-tutorial). O projeto Django mantém o nome `app` e a aplicação `core` preserva o usuário customizado e suas migrações originais.

## Requisitos

- Python 3.12 ou 3.13
- PDM

## Executar localmente

No PowerShell:

```powershell
Copy-Item .env.example .env
pdm install
pdm run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
# Substitua SECRET_KEY em .env pelo valor gerado acima.
pdm run migrate
pdm run check
pdm run dev
```

Servidor: <http://127.0.0.1:8000/>. A documentação da API está em <http://127.0.0.1:8000/api/doc/>. O SQLite local é criado em `db.sqlite3`, ignorado pelo Git. As origens permitidas pelo CORS vêm de `FRONTEND_URLS` no `.env`.

## Conteúdo do portfólio

O cadastro e a edição são feitos em <http://127.0.0.1:8000/admin/> por um usuário com acesso ao Admin. Cadastre primeiro as tecnologias em **Core → Tecnologias**; depois, em **Core → Projetos**, informe título, resumo e ano, selecione as tecnologias e envie a imagem opcional. O slug é sugerido a partir do nome ou título e pode ser ajustado antes de salvar. Cadastre a trajetória em **Core → Experiências** e **Core → Formações**. Use `publicado` para controlar o que aparece na API. Nenhum registro é criado automaticamente.

Os endpoints públicos aceitam somente GET:

| Recurso | Caminho |
| --- | --- |
| Projetos | `/api/projetos/` |
| Projeto por slug | `/api/projetos/{slug}/` |
| Tecnologias | `/api/tecnologias/` |
| Experiências | `/api/experiencias/` |
| Formações | `/api/formacoes/` |

Use `/api/projetos/?destaque=true` ou `/api/projetos/?destaque=false` para filtrar projetos. Projetos, experiências e formações não publicados são ocultados inclusive nas páginas de detalhe. As listagens usam paginação (`results`, `page`, `page_size`, `total_pages`). A imagem de projeto é servida em `/media/` durante o desenvolvimento; em produção, configure o armazenamento e a entrega de mídia conforme o ambiente.
