from rest_framework import viewsets
from .models import Review
from .serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filterset_fields = ['user', 'service', 'booking', 'rating']
    search_fields = ['comment']
    ordering_fields = ['rating', 'created_at']