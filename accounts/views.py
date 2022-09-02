from rest_framework import generics
from .models import Account
from .serializers import AccountSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import IsAccountOwnerOrReadOnly


class AccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountSortedView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        num = self.kwargs["num"]
        return self.queryset.order_by("date_joined")[0:num]


class AccountDetailView(generics.RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAccountOwnerOrReadOnly,
    ]


class AccountDetailProtectedView(generics.RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]
