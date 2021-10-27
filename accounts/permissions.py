from rest_framework import permissions

class ListPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return False

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.id==obj.id
