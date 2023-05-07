from django.urls import path

from oscar import config


class Shop(config.Shop):
    name = 'oscar'
