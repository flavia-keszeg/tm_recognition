from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework.routers import DefaultRouter

from quickstart import views

router = DefaultRouter()

router.register(r'object_recognition', views.ObjectRecognitionViewSet, basename='object-recognition')
router.register(r'face_recognition', views.FaceRecognitionViewSet, basename='face-recognition')
urlpatterns = router.urls

urlpatterns += [
    path('social_distancing_page/', views.social_distancing_page, name='social_distancing_page'),
    path('selfie_time_page/', views.selfie_time_page, name='selfie_time_page'),
    path('recognised_people/', views.recognised_people, name='recognised_people_page')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
