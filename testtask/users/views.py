from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import CarSerializer, CustomUserRegisterationSerializer, CustomUserLoginSerializer, \
    CustomUserSerializer, CustomUserProfileSerializer
from .models import Car, CustomUser

User = get_user_model()


class UserRegisterationAPIView(GenericAPIView):
    """
    Used to register new users. After successful registration, you can get a jwt token
    """
    permission_classes = (AllowAny,)
    serializer_class = CustomUserRegisterationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(GenericAPIView):
    """
    Used to log in to your account. After successfully logging in, you can get a jwt token
    """
    permission_classes = (AllowAny,)
    serializer_class = CustomUserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = CustomUserSerializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_200_OK)


class UserLogoutAPIView(GenericAPIView):
    """
    Used to log out of the account
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(RetrieveUpdateAPIView):
    """
    Used to get information about the current account. A jwt token is required
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user


class CarApi(APIView):
    """
    Cars API
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """
        Used to get a list of the user's cars
        """
        user_id = request.user.id
        all_cars = Car.objects.filter(owner__id=user_id)
        serialized_all_cars = CarSerializer(all_cars, context={"request": request}, many=True)
        return Response(serialized_all_cars.data)

    def post(self, request):
        """
        Used to add a new car for the user
        """
        car = request.data
        user_id = request.user.id
        car['owner'] = user_id
        serializer = CarSerializer(data=car)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"status": 200})
