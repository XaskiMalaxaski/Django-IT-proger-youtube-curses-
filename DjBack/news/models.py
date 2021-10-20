from django.db import models


class Articles(models.Model):
    title = models.CharField('Name', max_length=50, default="name_news")
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Text')
    date = models.DateTimeField('Date publication')

    def __str__(self):
        return f'New: {self.title}'

    class Meta:
        verbose_name = 'New'
