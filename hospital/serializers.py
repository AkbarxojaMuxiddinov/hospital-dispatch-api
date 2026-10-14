from rest_framework import serializers
from .models import *

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class AmbulanceSerializer(serializers.ModelSerializer):
    hospital_name = serializers.CharField(source="Bolnitsa_nomi", read_only=True)
    driver_username = serializers.CharField(source="Haydovchi_ismi", read_only=True)

    class Meta:
        model =  Ambulance
        fields = '__all__'




class EmergencyCallSerializer(serializers.ModelSerializer):
    patient_username = serializers.CharField(source="Bemor_ismi", read_only=True)
    ambulance_plate = serializers.CharField(source="Palata raqami", read_only=True)


    class Meta:
        model = EmergencyCall
        fields = '__all__'
        read_only_fields = ('status', 'ambulance', 'patient')
