"""Rotas iniciais do projeto."""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from core.views import ExperienciaViewSet, FormacaoViewSet, ProjetoViewSet, TecnologiaViewSet

router = DefaultRouter()
router.register(r'projetos', ProjetoViewSet, basename='projetos')
router.register(r'tecnologias', TecnologiaViewSet, basename='tecnologias')
router.register(r'experiencias', ExperienciaViewSet, basename='experiencias')
router.register(r'formacoes', FormacaoViewSet, basename='formacoes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/doc/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
