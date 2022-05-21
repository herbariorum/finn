from peewee import *
from database.BaseModel import BaseModel
import datetime


class Aluno(BaseModel):
    id = AutoField()
    nome = CharField(max_length=80)
    cpf = CharField(max_length=11)
    rg = CharField(max_length=15)
    orgao_exp_rg = CharField(15)
    uf_exp_rg = CharField(2)
    nascimento = DateField()
    sexo = CharField(10)
    pai = IntegerField()
    mae = IntegerField()
    endereco = CharField()
    bairro = CharField(80)
    cidade = CharField(80)
    uf = CharField(2)

    uf_naturalidade = CharField(2)
    naturalidade = CharField()
    nacionalidade = CharField()
    certidao_nascimento = CharField()
    termo_certidao_nasc = CharField()
    folha_certidao_nasc = CharField()
    livro_certidao_nasc = CharField()
    data_emissao_certidao = DateField()
    cartorio_certidao = CharField()

    photo = BlobField()
    criadoem = DateField(default=datetime.date.today())
    atualizadoem = DateField()