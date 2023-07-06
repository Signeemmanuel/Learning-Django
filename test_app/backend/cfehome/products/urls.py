from django.urls import path
from .views import ProductDetails, ProductListCreateAPIView, ProductUpdate,  ProductDestroy, product_all_views

urlpatterns = [
    path('', ProductListCreateAPIView.as_view(), name='create-product'),
    path('<int:pk>/', ProductDetails.as_view(), name="product-details"),
    path('<int:pk>/update/', ProductUpdate.as_view(), name="product-update"),
    path('<int:pk>/delete/', ProductDestroy.as_view(), name="product-destroy"),
    path('allviews/', product_all_views, name="create-product-all-views"),
    path('allviews/<int:pk>/', product_all_views, name="details-product-all-views"),
]
