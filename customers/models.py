from django.db import models

# Create your models here.
class UserContacts(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'