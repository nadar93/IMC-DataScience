from rest_framework import serializers
from api.models import Post


class NoteSerializer(serializers.Serializer):
    post = serializers.CharField(max_length=200)

    def create(self, validated_data):
        """
        Create and return a new `Note` instance, given the validated data.
        """
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Note` instance, given the validated data.
        """
        instance.title = validated_data.get('post', instance.title)
        instance.save()
        return instance
