from rest_framework import mixins, viewsets


class GetCreateViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    pass
