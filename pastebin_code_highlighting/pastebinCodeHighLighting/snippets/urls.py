from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetList, SnippetDetail, snippet_list, snippet_detail

urlpatterns = [
    path('snippets/', snippet_list, name='snipped_list'),
    path('snippets/<int:pk>', snippet_detail, name='snippet_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
