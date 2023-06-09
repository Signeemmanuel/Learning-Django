from django.urls import path
from .views import ProductDetails, ProductListCreateAPIView, ProductUpdate,  ProductDestroy, product_all_views

urlpatterns = [
    path('', ProductListCreateAPIView.as_view(), name='create_product'),
    path('<int:pk>/', ProductDetails.as_view(), name="product_details"),
    path('<int:pk>/update/', ProductUpdate.as_view(), name="product_update"),
    path('<int:pk>/delete/', ProductDestroy.as_view(), name="product_destroy"),
    path('allviews/', product_all_views, name="create_product_all_views"),
    path('allviews/<int:pk>/', product_all_views, name="details_product_all_views"),
]
