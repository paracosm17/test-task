from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.UserRegisterationAPIView.as_view(), name="create-user"),
    path("login/", views.UserLoginAPIView.as_view(), name="login-user"),
    path("logout/", views.UserLogoutAPIView.as_view(), name="logout-user"),
    path("user/", views.UserAPIView.as_view(), name="user-info"),
    path("cars/", views.CarApi.as_view(), name="cars"),
]
