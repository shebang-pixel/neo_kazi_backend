from django.db import models

class Invoice(models.Model):
    booking = models.OneToOneField('bookings.Booking', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, default='pending') # pending, paid, failed
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    transaction_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    issued_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Invoice {self.id} - {self.booking.user.email}"
    
class Payment(models.Model):
    invoice = models.ForeignKey('invoices.Invoice', on_delete=models.CASCADE)
