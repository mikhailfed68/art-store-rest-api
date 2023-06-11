from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractProduct

from authors.models import Painter


class Product(AbstractProduct):
    author = models.ForeignKey(
        Painter, on_delete=models.CASCADE,
        verbose_name='Автор', related_name='artworks',
        null=True, blank=True,
    )


# import at the end of the file allows the classes
# specified above to be instantiated correctly.
# this crutch was dictade by django-oscar docs
from oscar.apps.catalogue.models import *  # noqa isort:skip
