from rest_framework import permissions


class IsPatient(permissions.BasePermission):


    def has_permission(self, request, view) -> bool:
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.role == 'PATIENT'
        )


class IsDriver(permissions.BasePermission):


    def has_permission(self, request, view) -> bool:
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.role == 'DRIVER'
        )


class IsAdminOrDoctor(permissions.BasePermission):


    def has_permission(self, request, view) -> bool:
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.role in ['ADMIN', 'DOCTOR']
        )


class IsEmergencyCallParticipantOrAdmin(permissions.BasePermission):


    def has_object_permission(self, request, view, obj) -> bool:

        if request.user.role in ['ADMIN', 'DOCTOR']:
            return True


        if request.user.role == 'PATIENT':
            return obj.patient == request.user


        if request.user.role == 'DRIVER':
            return obj.ambulance and obj.ambulance.driver == request.user

        return False