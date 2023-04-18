from typing import Protocol, OrderedDict

from django.db.models import QuerySet

from . import repos, models


class UserServicesInterface(Protocol):

    def get_users(self) -> QuerySet[models.CustomUser]: ...

    def create_user(self, data: OrderedDict) -> QuerySet[models.CustomUser]: ...

    def update_user(self, pk: int, data: OrderedDict) -> QuerySet[models.CustomUser]: ...


class UserServicesV1:
    user_repos: repos.UserReposInterface = repos.UserReposV1()

    def get_users(self) -> QuerySet[models.CustomUser]:
        return self.user_repos.get_users()

    def create_user(self, data: OrderedDict) -> QuerySet[models.CustomUser]:
        return self.user_repos.create_user(data=data)

    def update_user(self, pk: int, data: OrderedDict) -> QuerySet[models.CustomUser]:
        return self.user_repos.update_user(pk, data)

