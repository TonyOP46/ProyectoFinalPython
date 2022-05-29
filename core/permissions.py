from tkinter.tix import Tree
from rest_framework import permissions

class OnlyLibrarian(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff == True:
           return Tree
        return obj == request.user


