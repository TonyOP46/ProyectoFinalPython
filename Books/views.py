from django.shortcuts import render
from rest_framework import viewsets
from .serializer import BookSerializer
from .models import books
from .permissions import IsOwnerReadOnly
from rest_framework.permissions import IsAdminUser
# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = books.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsOwnerReadOnly]
        return [permission() for permission in permission_classes]
        