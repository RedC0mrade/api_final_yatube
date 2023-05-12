from django.urls import include, path
from rest_framework import routers

from.views import CommentViewSet, GroupViewSet, FollowViewSet, PostViewSet

v1_router = routers.DefaultRouter()
v1_router.register(r'posts', PostViewSet, basename='posts')
v1_router.register(r'groups', GroupViewSet, basename='groups')
v1_router.register(r'follow', FollowViewSet, basename='follow')
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')


urlpatterns = [
    path('v1/', include(v1_router.urls))
]
