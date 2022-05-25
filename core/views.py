from django.shortcuts import render
from .permissions import IsOwnerReadOnly
from .models import User
from rest_framework import viewsets
from .serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.
from rest_framework.decorators import action
from Books.models import books
from Books.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from library.models import RackItem
from Books.models import books

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsOwnerReadOnly]
        return [permission() for permission in permission_classes]


    @action(detail=True)
    def my_books(self, request, pk=None):
        queryset = books.objects.filter(
            owner__id= pk
        )
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    @action(detail=True)
    def my_books_on_stand(self, request, pk=None):
        queryset = RackItem.objects.filter(
            Books__owner__id=pk
        ).values_list("Books__id", flat=True)
        book = books.objects.filter(
            id__in=queryset
        )
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





