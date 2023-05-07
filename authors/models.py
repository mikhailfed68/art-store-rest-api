from django.db import models

from sorl import thumbnail


def get_directory_path_for_avatar(instance, filename):
    return f'painters/painter_{instance.id}/avatar/{filename}'


class Painter(models.Model):
    """A model of painter on site."""

    first_name = models.CharField('Имя', max_length=16)
    last_name = models.CharField('Фамилия', max_length=16)
    birthday = models.DateField('Дата рождения')
    about_yourself = models.TextField('О себе')
    avatar = thumbnail.ImageField('Аватар', upload_to=get_directory_path_for_avatar)
    education = models.CharField('Образование', max_length=160)
    exhibitions = models.ManyToManyField('Exhibition', verbose_name='Выставки', blank=True)
    tags = models.ManyToManyField('Tag', verbose_name='Теги', blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}' # amend to 3th version

    def count_artworks(self):
        return self.artworks.count()

class Tag(models.Model):
    name = models.CharField('Название', max_length=30)

    def __str__(self) -> str:
        return self.name


class Exhibition(models.Model):
    name = models.CharField('Название', max_length=160)
    description = models.TextField('Описание')
    date = models.DateField('Дата')

    def __str__(self) -> str:
        return self.name
