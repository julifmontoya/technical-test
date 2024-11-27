from rest_framework import serializers
from .models import Product, ProductBatch, Transaction
from django.core.exceptions import ValidationError
from django.utils import timezone

class ProductSerializer(serializers.ModelSerializer):
    total_quantity = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = ['id', 'code', 'name', 'total_quantity']

class ProductBatchSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()

    class Meta:
        model = ProductBatch
        fields = ['id', 'product', 'expiration_date', 'quantity', 'status']

    def validate_expiration_date(self, value):
        # Validate if expiration date is before today
        today = timezone.now().date()
        if value <= today:
            raise ValidationError("The expiration date must be in the future.")
        return value    

# Inheriting from ProductBatchSerializer
class FlatProductBatchSerializer(ProductBatchSerializer):
    code = serializers.CharField(source='product.code')
    name = serializers.CharField(source='product.name')

    class Meta(ProductBatchSerializer.Meta):
        fields = ProductBatchSerializer.Meta.fields + ['code', 'name']

class TransactionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['batch', 'transaction_type', 'quantity']

    def validate_quantity(self, value):
        if value <= 0:
            raise ValidationError("Quantity must be a positive number.")
        return value

class TransactionSerializer(serializers.ModelSerializer):
    code = serializers.CharField(source='batch.product.code', read_only=True)
    name = serializers.CharField(source='batch.product.name', read_only=True)
    total_quantity = serializers.IntegerField(source='batch.product.total_quantity', read_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'batch', 'transaction_type', 'quantity', 'code', 'name', 'total_quantity', 'timestamp']
