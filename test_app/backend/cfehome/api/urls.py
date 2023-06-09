from django.urls import path
from .views import api_home, api_post

urlpatterns = [
    path("api_home/", api_home, name='api_home'),
    path("api_post/", api_post, name="api_post"),
]