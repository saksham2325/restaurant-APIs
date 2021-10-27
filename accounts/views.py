from rest_framework import authentication
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts import permissions as custompermission
from accounts import serializers
from accounts.models import User


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_name': user.name,
            'email': user.email
        })


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response({'message': 'User is logout'})


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [custompermission.ListPermission]
        else:
            permission_classes = [permissions.IsAuthenticated, custompermission.IsOwner]
        return [permission() for permission in permission_classes]

