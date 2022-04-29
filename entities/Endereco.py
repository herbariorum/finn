from peewee import *
from database.BaseModel import BaseModel


class Endereco(BaseModel):

    logradouro = CharField(null=False)
    numero = IntegerField()
    bairro = CharField(max_length=80)
    cidade = CharField()
    estado = CharField(max_length=2)
    cep = CharField(max_length=8)