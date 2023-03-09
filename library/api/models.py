from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    annotation = models.TextField(max_length=600, default='SOME STRING')
    author = models.CharField(max_length=20, default='SOME STRING')
    completed = models.BooleanField(default =False, blank=True, null=True)

    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Библиотека'

    def __str__(self):
        return self.title