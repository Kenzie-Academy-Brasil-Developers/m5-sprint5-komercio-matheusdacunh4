from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Product


class IsProductOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Product):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.seller == request.user
    

class IsSellerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_seller
