from peewee import *
from database.BaseModel import BaseModel


class User(BaseModel):
    id = AutoField()
    nome = CharField(max_length=80)
    nick = CharField()
    email = CharField(unique=True)
    password = CharField()
    criadoem = DateField()
    atualizadoem = DateField()

    @property
    def serialize(self):
        data = {
            'id': self.id,
            'nome': self.nome,
            'nick': self.nick,            
        }
        return data

    def __repr__(self):
        return "Usuários {}".format(self.nome)