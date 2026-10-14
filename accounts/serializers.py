from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role', 'phone_number')

    def create(self, validated_data):
        
        password = validated_data.pop('password', None)


        user = User.objects.create(**validated_data)


        if password:
            user.set_password(password)
            user.save()

        return user