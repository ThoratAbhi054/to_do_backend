from django.urls import include
from django.urls import path
from rest_framework import routers

from iam.user.views import CustomTokenObtainPairView
from iam.user.views import RegisterView
from iam.user.views import UserProfileViewSet


router = routers.SimpleRouter()
router.register(r"iam", UserProfileViewSet, basename="iam")

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),
    path("signup/", RegisterView.as_view(), name="signup"),
    path("", include(router.urls)),
]
