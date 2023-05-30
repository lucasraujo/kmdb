from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that username already exists.",
            )
        ]
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="user with this email already exists.",
            )
        ],
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "bio",
            "is_critic",
            "is_superuser",
            "updated_at"
        ]

        read_only_fields = ["is_superuser", "updated_at", "id"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)
