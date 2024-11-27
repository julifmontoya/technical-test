from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.exceptions import ValidationError
from .models import Product, ProductBatch, Transaction
from .serializers import ProductSerializer, FlatProductBatchSerializer, ProductBatchSerializer, TransactionCreateSerializer, TransactionSerializer


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreate(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductBatchList(ListAPIView):
    serializer_class = FlatProductBatchSerializer

    def get_queryset(self):
        # Fetch all batches and ensure the related product information is included
        return ProductBatch.objects.select_related('product').order_by('product__name', 'expiration_date')


class ProductBatchDetail(ListAPIView):
    serializer_class = ProductBatchSerializer

    def get_queryset(self):
        product_code = self.kwargs.get('product_code')
        queryset = ProductBatch.objects.filter(product__code=product_code).order_by('expiration_date')
        #print(str(queryset.query))  
        return queryset

class ProductBatchCreate(CreateAPIView):
    queryset = ProductBatch.objects.all()
    serializer_class = ProductBatchSerializer


class TransactionList(ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionCreate(CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionCreateSerializer

    def perform_create(self, serializer):
        transaction = serializer.save()
        batch = transaction.batch

        # Validate the transaction logic
        if transaction.transaction_type == 'exit' and batch.quantity < transaction.quantity:
            raise ValidationError(
                "Not enough stock in this batch to make this exit.")

        # Update the batch quantity based on the transaction type
        if transaction.transaction_type == 'entry':
            batch.quantity += transaction.quantity
        elif transaction.transaction_type == 'exit':
            batch.quantity -= transaction.quantity

        # Save the batch with the updated quantity
        batch.save()
        return transaction
