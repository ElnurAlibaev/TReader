from django.db import models
from django.utils.translation import gettext_lazy as _


class BookTypeChoices(models.TextChoices):
    Manga = _("Манга")
    Manhwa = _("Манхва")
    Manhua = _("Маньхуа")
