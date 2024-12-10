from django.db import models

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='Название', unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = [
            'name',
        ]

    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    deadline = models.DateTimeField(null=True, blank=True, verbose_name='Срок')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    is_done = models.BooleanField(default=False, verbose_name='Выполнено')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания') 
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = [
            '-created_at',
        ]
    def __str__(self):
        return self.title
