from django.db import models
from django.utils import timezone
from datetime import timedelta
import uuid

class Product(models.Model):
    code = models.CharField(max_length=10, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.code})"

    @property
    def total_quantity(self):
        """Calculate the total stock from all batches."""
        return sum(batch.quantity for batch in self.batches.all())

class ProductBatch(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='batches')
    expiration_date = models.DateField()
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.product.name} ({self.product.code}) - {self.expiration_date} (Qty: {self.quantity})"

    @property
    def status(self):
        """Status of the individual batch."""
        today = timezone.now().date()
        if self.expiration_date < today:
            return "Expired"
        elif self.expiration_date <= today + timedelta(days=3):
            return "Expiring"
        else:
            return "Current"

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('entry', 'Entry'),
        ('exit', 'Exit'),
    )

    batch = models.ForeignKey(ProductBatch, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.transaction_type.capitalize()} {self.quantity} of {self.batch.product.name} (Batch: {self.batch.id})"
