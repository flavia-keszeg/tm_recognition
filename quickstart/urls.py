from rest_framework.routers import DefaultRouter

from quickstart.views import ObjectRecognitionViewSet, FaceRecognitionViewSet

router = DefaultRouter()

router.register(r'object_recognition', ObjectRecognitionViewSet, basename='object-recognition')
router.register(r'face_recognition', FaceRecognitionViewSet, basename='face-recognition')
urlpatterns = router.urls