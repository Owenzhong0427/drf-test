"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import IsAdminUser
from rest_framework.schemas import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import root

auth_urlpatterns = [
    path('', obtain_jwt_token, name='get-token'),
    path('refresh/', refresh_jwt_token, name='refresh-token'),
]

api_urlpatterns = [
    path('', include('apps.musics.urls')),
]

urlpatterns = [
    path('', root, name='root'),
    path('admin/', admin.site.urls),
    path('api/', include((api_urlpatterns, 'api'))),
    path('api/auth/', include((auth_urlpatterns, 'api-auth'))), 
    path('docs/', include_docs_urls(
        title='Owen_drt_api',
        permission_classes=[IsAdminUser]
    )),    
]
