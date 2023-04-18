from rest_framework import serializers
from . import models


class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = ('first_name', 'last_name', 'username', )


class RetrieveCreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = '__all__'


