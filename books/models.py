import csv
import uuid

from django.db import models
from . import choices


class Genre(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, auto_created=True)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=500, default='Image')
    score = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField(default='SomeDescription')
    book_type = models.CharField(max_length=10,
                                 choices=choices.BookTypeChoices.choices,
                                 default=choices.BookTypeChoices.Manga)

    release_date = models.IntegerField()
    update_date = models.DateTimeField(auto_now=True)

    genres = models.ManyToManyField(
        to=Genre,
        related_name='genres',
        blank=True
    )

    tags = models.ManyToManyField(
        to=Tag,
        related_name='tags',
        blank=True
    )

    def __str__(self):
        return self.title


class Source(models.Model):
    book = models.ForeignKey(
        to=Book,
        on_delete=models.PROTECT,
        related_name='sources',
        default=None
    )
    title = models.CharField(max_length=100)
    chapters = models.IntegerField(default=0)
    link = models.CharField(max_length=300, default='SomeLink')

    def __str__(self):
        return self.title


#Data-Generator
