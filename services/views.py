from rest_framework import viewsets
from .models import Service
from .serializers import ServiceSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filterset_fields = ['category', 'provider', 'is_active']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']