from database.ResponsavelDataSet import ResponsavelDataSet as dataset
from entities.Responsavel import Responsavel


def selectAll():
    return dataset.selectAll(Responsavel)
   

def selectById(id):
    return dataset.selectById(Responsavel, id)

def search(texto):
    return dataset.search(Responsavel, texto)

def verificaCPFExiste(cpf):
    return dataset.findByCpf(Responsavel, cpf)

def insert(registros):
    return dataset.create(Responsavel, registros)

def update(registros):
    return dataset.update(Responsavel, registros)

def delete(id):
    return dataset.delete(Responsavel, id)

def selectForPage(page, number_for_page):
    return dataset.selectPerPage(Responsavel, page, number_for_page)

