from django.db import models


class Meaning(models.Model):
    meaning = models.CharField(max_length=510, verbose_name='Значение')
    meta = models.CharField(max_length=10, verbose_name='Мета')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    class Meta:
        verbose_name = 'Значение'
        verbose_name_plural = 'Значения'

    def __str__(self):
        return self.meaning


class Phrase(models.Model):
    phrase = models.CharField(max_length=510, verbose_name='Словосочетание')
    meaning = models.ForeignKey(Meaning, on_delete=models.CASCADE, verbose_name='Значение')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    class Meta:
        verbose_name = 'Фраза'
        verbose_name_plural = 'Фразы'

    def __str__(self):
        return f'{self.phrase} - {self.meaning}'

    def as_dict(self):
        return {
            'id': self.pk,
            'phrase': self.phrase,
            'meaning': self.meaning.meaning
        }