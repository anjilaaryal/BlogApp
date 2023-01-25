from rest_framework import serializers


class AddPostRequest(serializers.Serializer):
    title = serializers.CharField(max_length = 100)
    description = serializers.CharField(max_length = 1000)