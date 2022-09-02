from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer, ProducDetailSerializer
from .utils.mixins import SerializerByMethodMixin
from .permissions import IsProductOwnerOrReadOnly, IsSellerOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProductView(SerializerByMethodMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_map = {
        "GET": ProductSerializer,
        "POST": ProducDetailSerializer,
    }

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsSellerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class ProductDetailView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProducDetailSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsSellerOrReadOnly,
        IsProductOwnerOrReadOnly,
    ]
