from rest_framework import serializers


class ObjectRecognitionSerializer(serializers.Serializer):
    image = serializers.ImageField()


class FaceRecognitionSerializer(serializers.Serializer):
    image = serializers.ImageField()
