# import peewee
# from entities.User import User
# from entities.Responsavel import Responsavel
# from entities.Contatos import Contatos
# from entities.Endereco import Endereco
# from database.BaseModel import db

# if __name__=='__main__':
#     try:
#         Responsavel.create_table()
       
#     except peewee.OperationalError:
#         print('Tabela já existe')

import controller.AlunoController as alunoController

import datetime
row = alunoController.selectById(1)

nascimento = row.nascimento

print(nascimento.strftime("%d/%m/%Y"))