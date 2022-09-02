from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "is_seller",
            "date_joined",
            "is_superuser",
            "is_active",
        ]

        read_only_field = ["id", "date_joined", "is_superuser", "is_active"]

        extra_kwargs = {
            "password": {"write_only": True},
            "is_seller": {"required": True},
        }

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)
