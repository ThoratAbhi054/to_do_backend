from django.contrib.auth.models import User
from rest_framework import serializers

from iam.user.models import UserProfile



class UserProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False, source="user.first_name")
    last_name = serializers.CharField(required=False, source="user.last_name")
    email = serializers.EmailField(required=False, source="user.email")

    class Meta:
        model = UserProfile
        fields = [
            "first_name",
            "last_name",
            "email",
            "contact_no",
            "city",
            "address",
            "avatar",
        ]


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "profile"]
