from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=50)
    address = models.CharField('Endereço', max_length=150)
    phone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('Email')
    
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.first_name} {self.last_name}'