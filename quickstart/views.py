from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from quickstart.recognition.face_recognition.face_recognition import face_recognition
from quickstart.recognition.object_recognition.object_recognition import object_recognition
from quickstart.serializers import ObjectRecognitionSerializer, FaceRecognitionSerializer


class ObjectRecognitionViewSet(viewsets.ViewSet):
    serializer_class = ObjectRecognitionSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        deserialized_data = serializer.validated_data

        image = deserialized_data["image"]

        detected_objects = object_recognition(image)

        return Response({
            'response': detected_objects
        })


class FaceRecognitionViewSet(viewsets.ViewSet):
    serializer_class = FaceRecognitionSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        deserialized_data = serializer.validated_data

        image = deserialized_data["image"]

        recognized_faces = face_recognition(image)

        return Response({
            'response': recognized_faces
        })

def main_page(request):
    return render(request, 'main_page.html', {})

def selfie_time_page(request):
    return render(request, 'selfie_time_page.html', {})

def social_distancing_page(request):
    return render(request, 'social_distancing_page.html', {})


