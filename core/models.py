from django.db import models

# Create your models here.


SEX_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
]


class Cliente(models.Model):

    nome = models.CharField('nome', max_length=50)
    sexo = models.CharField('Sexo', max_length=1, choices=SEX_CHOICES)
    cpf = models.CharField('CPF', max_length=15)
    nasc = models.DateField('Nascimento', max_length=10)
    telefone = models.CharField('Telefone', max_length=15)
    celular = models.CharField('Celular', max_length=15)
    email = models.EmailField('E-mail', default=None)

    class Meta:
        verbose_name = ('Cliente')
        verbose_name_plural = ('Clientes')

    def __str__(self):
        return self.nome



