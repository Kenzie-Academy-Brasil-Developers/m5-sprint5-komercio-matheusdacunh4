from rest_framework import serializers

from .models import Product
from accounts.serializers import AccountSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["description", "price", "quantity", "is_active", "seller_id"]


        read_only_field = ["description", "price", "quantity", "is_active", "seller_id"]


class ProducDetailSerializer(serializers.ModelSerializer):
    seller = AccountSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ["id", "seller", "description", "price", "quantity", "is_active"]

        read_only_field = ["is_active", "id"]
