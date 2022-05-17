# from database.AlunoDataset import AlunoDataSet as dataset
from entities.Aluno import Aluno
from database.DataSet import DataSet as dataset


def selectAll():
    return dataset.selectAll(Aluno)

def selectById(id):
    return dataset.selectById(Aluno, id)

def search(texto):
    return dataset.search(Aluno, texto)