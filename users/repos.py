from typing import Protocol, OrderedDict
from django.db.models import QuerySet
from . import models


class UserReposInterface(Protocol):

    @staticmethod
    def get_users(self) -> QuerySet[models.CustomUser]: ...

    @staticmethod
    def create_user(self, data: OrderedDict) -> QuerySet[models.CustomUser]: ...

    @staticmethod
    def update_user(self, pk: int, data: OrderedDict) -> QuerySet[models.CustomUser]: ...


class UserReposV1:

    @staticmethod
    def get_users() -> QuerySet[models.CustomUser]:
        return models.CustomUser.objects.all()

    @staticmethod
    def create_user(data: OrderedDict) -> models.CustomUser:
        return models.CustomUser.objects.create_user(**data)

    @staticmethod
    def update_user(pk: int, data: OrderedDict) -> QuerySet[models.CustomUser]:
        return models.CustomUser.objects.filter(id=pk).update(username=data['username'], first_name=data['first_name'],
                                                              last_name=data['last_name'])
