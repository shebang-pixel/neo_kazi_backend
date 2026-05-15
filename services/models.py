from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_duration = models.DurationField(blank=True, null=True) # e.g., for "2 hours"
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='services')
    provider = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='provided_services')
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Services"
