from database.ResponsavelDataSet import ResponsavelDataSet as dataset
from entities.Responsavel import Responsavel

retorno = dataset.selectById(Responsavel, 1)
print(retorno.nome)