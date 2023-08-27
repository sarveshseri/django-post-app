from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    id = serializers.UUIDField(allow_null=False, read_only=True)
    content = serializers.CharField(allow_null=False, allow_blank=True)
    created_at = serializers.DateTimeField(allow_null=False)


class PostCreateSerializer(serializers.Serializer):
    id = serializers.UUIDField(allow_null=False)
    content = serializers.CharField(allow_null=False, allow_blank=True)


class PostAnalysisSerializer(serializers.Serializer):
    word_count = serializers.IntegerField(read_only=True, allow_null=False)
    average_word_size = serializers.FloatField(read_only=True, allow_null=False)
