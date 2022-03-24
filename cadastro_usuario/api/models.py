from django.db import models
from django.db.models.fields import CharField


class Usuario(models.Model):
    login = CharField('LOGIN', max_length=40, null=False)
    senha = CharField('SENHA', max_length=40, null=True)
    data_nascimento = models.DateField('DATA_NASCIMENTO', null=False)
