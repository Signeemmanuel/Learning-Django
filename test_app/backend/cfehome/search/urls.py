from rest_framework.urls import path
from .views import SearchGenericView

urlpatterns = [
    path('', SearchGenericView.as_view(), name='search'),
]