from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .serializers import UserSerializer


class UserViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        user = {   
            "user": self.request.user, 
            "is_staff": str(self.request.user.is_staff),
        }
        serializer = UserSerializer(user)
        return Response(serializer.data)
