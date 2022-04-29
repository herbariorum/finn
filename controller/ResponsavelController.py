from database.ResponsavelDataSet import ResponsavelDataSet as dataset
from entities.Responsavel import Responsavel


def selectAll():
    return dataset.selectAll(Responsavel)
   
    

