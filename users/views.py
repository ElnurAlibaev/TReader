from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from . import serializers, services, permissions
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404


class UserViewSet1(ViewSet):
    user_services: services.UserServicesInterface = services.UserServicesV1()
    queryset = user_services.get_users()

    # pagination_class = pagination.CustomPageNumberPagination

    # filter_backends = (DjangoFilterBackend,)
    # filterset_class = filters.BookFilter

    permission_classes = [permissions.UserPermission,]

    def list(self, request):
        serializer = serializers.ListUserSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        self.check_object_permissions(request, user)
        serializer = serializers.RetrieveCreateUserSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        serializer = serializers.RetrieveCreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.user_services.create_user(data=serializer.validated_data)
        return Response(serializer.validated_data)
