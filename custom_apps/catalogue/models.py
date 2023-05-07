from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractProduct

from authors.models import Painter


class Product(AbstractProduct):
    author = models.ForeignKey(
        Painter, on_delete=models.CASCADE,
        verbose_name='Автор', related_name='artworks',
        null=True, blank=True,
    )


from oscar.apps.catalogue.models import *  # noqa isort:skip
