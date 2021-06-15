from rest_framework.serializers import Serializer, CharField


class UserSerializer(Serializer):
    user = CharField(max_length=200)
    is_staff = CharField(max_length=200)
