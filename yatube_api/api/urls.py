from django.urls import include, path
from rest_framework import routers

from.views import PostViewSet

v1_router = routers.DefaultRouter()
v1_router.register(r'posts', PostViewSet, basename='posts')


urlpatterns = [
    path('v1', include(v1_router.urls))
]
