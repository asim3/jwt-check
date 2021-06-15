from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .serializers import UserSerializer


class UserViewSet(ViewSet):
    def retrieve(self, request):
        user = {   
            "user": request.user, 
            "is_active": request.user.is_active,
            "is_staff": request.user.is_staff,
            "is_authenticated": request.user.is_authenticated,
            "is_superuser": request.user.is_superuser,
        }
        serializer = UserSerializer(user)
        return Response(serializer.data)


class AdminViewSet(ViewSet):
    def retrieve(self, request):
        user = {   
            "user": request.user, 
            "is_active": request.user.is_active,
            "is_staff": request.user.is_staff,
            "is_authenticated": request.user.is_authenticated,
            "is_superuser": request.user.is_superuser,
        }
        raise
        serializer = UserSerializer(user)
        return Response(serializer.data)
