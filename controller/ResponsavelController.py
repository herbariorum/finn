from database.ResponsavelDataSet import ResponsavelDataSet as dataset
from entities.Responsavel import Responsavel


def selectAll():
    return dataset.selectAll(Responsavel)
   

def selectById(id):
    return dataset.selectById(Responsavel, id)

def search(texto):
    return dataset.search(Responsavel, texto)
    

