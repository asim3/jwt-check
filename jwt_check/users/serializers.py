from rest_framework.serializers import Serializer, CharField, BooleanField, DictField


class UserSerializer(Serializer):
    user = CharField(max_length=200)
    is_active = BooleanField()
    is_staff = BooleanField()
    is_authenticated = BooleanField()
    is_superuser = BooleanField()
    auth = CharField(max_length=2000)
    headers = DictField()
