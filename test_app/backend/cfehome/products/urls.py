from django.urls import path
from .views import ProductDetails, ProductListCreateAPIView, product_all_views

urlpatterns = [
    path('', ProductListCreateAPIView.as_view(), name='create_product'),
    path('<int:pk>/', ProductDetails.as_view(), name="product_details"),
    path('allviews/', product_all_views, name="create_product_all_views"),
    path('allviews/<int:pk>/', product_all_views, name="details_product_all_views"),
]
