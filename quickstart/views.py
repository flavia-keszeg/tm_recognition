from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render

from quickstart.recognition.face_recognition.face_recognition import face_recognition
from quickstart.recognition.object_recognition.object_recognition import object_recognition, \
    calculate_total_nr_of_people
from quickstart.serializers import ObjectRecognitionSerializer, FaceRecognitionSerializer


class ResultImageViewSet(viewsets.ViewSet):
    def create(self):
        image_data = open("quickstart/recognition/object_recognition/imagenew.jpg", "rb").read()
        return HttpResponse(image_data, content_type="image/png")


class ObjectRecognitionViewSet(viewsets.ViewSet):
    serializer_class = ObjectRecognitionSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        deserialized_data = serializer.validated_data

        image = deserialized_data["image"]
        actual_size = deserialized_data["actual_size"]

        detected_people = object_recognition(image, actual_size)


        image_link = "http://127.0.0.1:8000/home/recognised_people/"
        return Response({
            'number of people with less than 2m between them': detected_people[0],
            'total number of people': detected_people[1],
            'picture': image_link
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


def recognised_people(request):
    return render(request, 'recognised_people.html', {})
