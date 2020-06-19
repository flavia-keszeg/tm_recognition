from rest_framework import serializers


class ObjectRecognitionSerializer(serializers.Serializer):
    image = serializers.ImageField()
    actual_size = serializers.IntegerField()


class FaceRecognitionSerializer(serializers.Serializer):
    image = serializers.ImageField()
