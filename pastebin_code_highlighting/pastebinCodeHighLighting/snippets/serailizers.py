from rest_framework import serializers

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        field = ['id', 'title', 'code', 'linenos' 'langauge', 'style']