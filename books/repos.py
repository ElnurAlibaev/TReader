from typing import Protocol
from django.db.models import QuerySet
from books import models


class BookReposInterface(Protocol):

    @staticmethod
    def get_books() -> QuerySet[models.Book]: ...


class BookReposV1:

    @staticmethod
    def get_books() -> QuerySet[models.Book]:
        return models.Book.objects.all()
