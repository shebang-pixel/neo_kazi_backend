from rest_framework import viewsets
from .models import Invoice, Payment
from .serializers import InvoiceSerializer, PaymentSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    filterset_fields = ['booking', 'payment_status', 'payment_method']
    search_fields = ['transaction_id']
    ordering_fields = ['amount', 'issued_at']

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filterset_fields = ['invoice']
    ordering_fields = ['id']
