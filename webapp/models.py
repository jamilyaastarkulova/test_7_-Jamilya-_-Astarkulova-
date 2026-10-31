from django.db import models

class Book(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активно'),
        ('blocked', 'Заблокировано'),
    ]
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    content = models.TextField(max_length=5000, null=False, blank=False, verbose_name="Контент")
    mail = models.EmailField(null=False, blank=False, verbose_name='Почта')
    status = models.CharField(choices=STATUS_CHOICES, default='active', related_name='books', null=False, blank=False, verbose_name='Статус')
    author = models.CharField(max_length=60, null=False, blank=False, default='Anonymous', verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f'{self.pk} - {self.title}'
