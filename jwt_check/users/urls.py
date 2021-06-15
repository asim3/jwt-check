from django.urls import path
from .views import UserViewSet, AdminViewSet


urlpatterns = [
    path('user/', UserViewSet.as_view({'get': 'retrieve'}), name='user_api'),
    path('admin/', AdminViewSet.as_view({'get': 'retrieve'}), name='admin_api'),
]
