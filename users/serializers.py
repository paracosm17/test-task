from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import CustomUser, Car


class CustomUserSerializer(serializers.ModelSerializer):
    cars = serializers.SerializerMethodField('get_cars')

    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "first_name", "last_name", "country", "cars")

    @staticmethod
    def get_cars(obj):
        return CarSerializer(Car.objects.filter(owner__id=obj.id), many=True).data


class CustomUserProfileSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    country = serializers.CharField(max_length=50)


class CustomUserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class CustomUserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("make", "model", "year", "color", "owner")

    def create(self, validated_data):
        return Car.objects.create(**validated_data)
