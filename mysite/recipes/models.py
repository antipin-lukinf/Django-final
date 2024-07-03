from django.db import models


# Рецепты:
# ○ Название
# ○ Описание
# ○ Шаги приготовления
# ○ Время приготовления
# ○ Изображение
# ○ Автор

class Recipes(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Описание')
    step = models.TextField(blank=True, verbose_name='Шаги приготовления')
    time = models.DateTimeField(verbose_name='Время приготовления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Изображение', blank=True)
    author = models.CharField(max_length=150, verbose_name='Автор')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['created_at']  # сортировка


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']  # сортировка
