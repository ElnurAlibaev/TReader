from django_filters import rest_framework as filters
from . import models


class BookFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    book_type = filters.CharFilter(field_name='book_type')
    tag = filters.CharFilter(method='filter_tag')
    genre = filters.CharFilter(field_name='filter_genre')

    class Meta:
        model = models.Book
        fields = ('title', 'book_type', 'tag', 'genre')

    def filter_tag(self, queryset, _, value):
        return queryset.filter(tags__title__contains=value)

    def filter_genre(self, queryset, _, value):
        return queryset.filter(genres__title__contains=value)
