from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'dictionaries/topics', views.TopicViewSet)

urlpatterns = [
    path('', include(router.urls)),
]