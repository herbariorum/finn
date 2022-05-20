# from database.AlunoDataset import AlunoDataSet as dataset
from entities.Aluno import Aluno
from database.DataSet import DataSet as dataset


def selectAll():
    return dataset.selectAll(Aluno)

def selectById(id):
    return dataset.selectById(Aluno, id)

def search(texto):
    return dataset.search(Aluno, texto)

def verificaCPFExiste(cpf):
    return dataset.findByCpf(Aluno, cpf)

def insert(registros):
    return dataset.create(Aluno, registros)

def update(registros):
    return dataset.update(Aluno, registros)

def delete(id):
    return dataset.delete(Aluno, id)

def selectForPage(page, number_for_page):
    return dataset.selectPerPage(Aluno, page, number_for_page)