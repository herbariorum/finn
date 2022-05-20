# from database.ResponsavelDataSet import ResponsavelDataSet as dataset
# from entities.Responsavel import Responsavel

# retorno = dataset.selectById(Responsavel, 1)
# print(retorno.nome)

from database.Connection import Conexao

con = Conexao()
db = con.conectaSQLITE()
db.open()

if not db.isOpen():
    print('Fechada')
    # db.close()
print('Aberta')
db.close()
    
