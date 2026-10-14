from rest_framework import viewsets, permissions
from .models import Hospital, Ambulance, EmergencyCall
from .serializers import HospitalSerializer, AmbulanceSerializer, EmergencyCallSerializer
from .permissions import IsAdminOrDoctor, IsEmergencyCallParticipantOrAdmin


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

    def get_permissions(self):

        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminOrDoctor]
        else:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]


class AmbulanceViewSet(viewsets.ModelViewSet):
    queryset = Ambulance.objects.all()
    serializer_class = AmbulanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'DRIVER':
            return Ambulance.objects.filter(driver=user)
        return Ambulance.objects.all()


class EmergencyCallViewSet(viewsets.ModelViewSet):
    queryset = EmergencyCall.objects.all()
    serializer_class = EmergencyCallSerializer

    def get_permissions(self):

        permission_classes = [permissions.IsAuthenticated, IsEmergencyCallParticipantOrAdmin]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'PATIENT':
            return EmergencyCall.objects.filter(patient=user)

        elif user.role == 'DRIVER':
            return EmergencyCall.objects.filter(ambulance__driver=user)

        return EmergencyCall.objects.all()

    def perform_create(self, serializer):

        patient = self.request.user


        available_ambulance = Ambulance.objects.filter(
            status=Ambulance.Status.AVAILABLE
        ).first()

        if available_ambulance:

            available_ambulance.status = Ambulance.Status.BUSY
            available_ambulance.save()


            serializer.save(
                patient=patient,
                ambulance=available_ambulance,
                status=EmergencyCall.CallStatus.DISPATCHED
            )
        else:

            serializer.save(
                patient=patient,
                status=EmergencyCall.CallStatus.PENDING
            )