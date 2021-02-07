from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ChartSerializer
from .models import Chart

# Create your views here.
class ChartViewSet(viewsets.ModelViewSet):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer
