from rest_framework.viewsets import ModelViewSet
from books import serializers, services, filters, pagination
from django_filters.rest_framework import DjangoFilterBackend


class BookViewSet1(ModelViewSet):
    book_services: services.BookServicesInterface = services.BookServicesV1()
    queryset = book_services.get_books()

    serializer_class = serializers.BookSerializer
    #pagination_class = pagination.CustomPageNumberPagination

    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.BookFilter
