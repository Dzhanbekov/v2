from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=20)
    anons = models.CharField('анонс', max_length=250)
    full_text = models.TextField('статья')
    data = models.DateTimeField('дата публикации')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'