from peewee import *
from database.BaseModel import BaseModel
from entities import Contatos, Endereco
import datetime


class Responsavel(BaseModel):
    id = AutoField()
    nome = CharField(max_length=80)
    cpf = CharField(max_length=11, unique=True)
    sexo = CharField(max_length=1)
    email = CharField()
    tipo_responsavel = CharField()
    profissao = CharField(max_length=100)
    # contato = IntegerField() # onetomany
    endereco = IntegerField() # onetoone
    status = IntegerField(default = 0)
    criadoem = DateField(default=datetime.date.today())
    atualizadoem = DateField(default=datetime.date.today)