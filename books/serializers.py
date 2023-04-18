from rest_framework import serializers
from books import models


class _BookGenresSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Genre
        fields = (
            'title',
        )


class _BookTagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag
        fields = (
            'title',
        )


class _BookSourcesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Source
        fields = (
            'title',
            'chapters',
        )


class BookSerializer(serializers.ModelSerializer):
    genres = _BookGenresSerializer(read_only=True, many=True)
    tags = _BookTagsSerializer(read_only=True, many=True)
    sources = _BookSourcesSerializer(read_only=True, many=True)

    class Meta:
        model = models.Book
        fields = '__all__'