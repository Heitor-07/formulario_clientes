from django.db import models

# Create your models here.


class Cliente(models.Model):

    nome = models.CharField('Nome', max_length=50)
    sexo = models.CharField('Sexo', max_length=15)
    cpf = models.CharField('CPF', max_length=11)
    nasc = models.DateField('Nascimento')
    telefone = models.CharField('Telefone', max_length=10)
    celular = models.CharField('Celular', max_length=11)
    email = models.EmailField('E-mail', default=None)

    class Meta:
        verbose_name = ('Cliente')
        verbose_name_plural = ('Clientes')

    def __str__(self):
        return self.nome



