from . import views
from django.urls import path

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:id>/', views.product_detail),
    path('collections/<int:pk>/', views.collection_detail, name='collection_detail'),
]