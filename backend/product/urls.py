from django.urls import path
from .views import (
    ProductList,
    ProductCreate,
    ProductBatchList,
    ProductBatchDetail,
    ProductBatchCreate,
    TransactionList, 
    TransactionCreate
)

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/create/', ProductCreate.as_view()),
    path('products/batches/', ProductBatchList.as_view()),      
    path('products/batches/create/', ProductBatchCreate.as_view()),
    path('products/batches/<str:product_code>/', ProductBatchDetail.as_view()),
    path('products/transactions/', TransactionList.as_view()),
    path('products/transactions/create/', TransactionCreate.as_view()),
]