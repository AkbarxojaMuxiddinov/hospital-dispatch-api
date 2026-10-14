from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HospitalViewSet, AmbulanceViewSet, EmergencyCallViewSet

router = DefaultRouter()
router.register(r'hospitals', HospitalViewSet, basename='hospital')
router.register(r'ambulances', AmbulanceViewSet, basename='ambulance')
router.register(r'calls', EmergencyCallViewSet, basename='emergency-call')

urlpatterns = [
    path('', include(router.urls)),
]