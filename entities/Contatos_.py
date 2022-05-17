from peewee import *
from database.BaseModel import BaseModel


class Contatos(BaseModel):
    id = AutoField()
    telefone = CharField(max_length=11)
    id_responsavel = IntegerField()
    