from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import MusicViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'musics', MusicViewSet)

urlpatterns = [
    path('', include(router.urls)),
]