from django.shortcuts import render
from .models import Music 
from rest_framework import viewsets, status
from .serializers import MusicSerializer
# Create your views here.


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer