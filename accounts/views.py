from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from accounts.serializers import UserSerializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        # print(request.data)
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


class UserViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
