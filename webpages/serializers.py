from rest_framework import serializers
from webpages.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'subtitle', 'content')
    """
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=128)
    subtitle = serializers.CharField(required=False, allow_blank=True, max_length=128)
    content = serializers.CharField(required=True, allow_blank=False)

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.subtitle = validated_data.get('subtitle', instance.subtitle)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
    """
