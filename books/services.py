from typing import Protocol, OrderedDict

from django.db.models import QuerySet

from books import repos, models


class BookServicesInterface(Protocol):
    book_repos: repos.BookReposInterface

    def get_books(self) -> QuerySet[models.Book]: ...


class BookServicesV1:
    book_repos: repos.BookReposInterface = repos.BookReposV1()

    def get_books(self) -> QuerySet[models.Book]:
        return self.book_repos.get_books()
