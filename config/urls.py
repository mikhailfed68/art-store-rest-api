"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.apps import apps
from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(
        title="Art-Vostorge Store Api",
        description="API for common functionality",
        version="1.0.0",
    )

swagger_view = TemplateView.as_view(
    template_name='swagger-ui.html',
    extra_context={'schema_url':'openapi-schema'}
    )

urlpatterns = [
    path('', include(apps.get_app_config('oscar').urls[0])),

    # the same endpoints to give priority to the custom api_root view
    path('api/', include('authors.urls')),
    path('api/', include('oscarapi.urls')),

    path('openapi/', schema_view, name='openapi-schema'),
    path('swagger-ui/', swagger_view, name='swagger-ui'),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
    path('__debug__/', include('debug_toolbar.urls')),
    ]
