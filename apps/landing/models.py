from django.db import models
from django_quill.fields import QuillField


class AboutUsPage(models.Model):
    content = QuillField(verbose_name='Контент')
    is_active = models.BooleanField(default=True, verbose_name='Активная')

    class Meta:
        verbose_name = 'Страница "О нас"'
        verbose_name_plural = 'Страницы "О нас"'
