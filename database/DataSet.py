from peewee import DoesNotExist

class DataSet:

    @staticmethod
    def selectAll(model):
        return model.select()

    @staticmethod
    def selectById(model, id):
        return model.select().where(model.id == id).get() # ou
        # return model.get(model.id == id)

    @staticmethod
    def selectByEmail(model, email):
        try:
            usuario = model.select().where(model.email == email).get()
        except DoesNotExist:
            return False
        return usuario
    
    @staticmethod
    def selectBySexo(model, valor):
        try:            
            usuario = model.select().where(model.sexo == valor)
        except DoesNotExist:
            return False
        return usuario
        
    @staticmethod
    def search(model, texto):
        return model.select().where(model.nome.contains(texto))

    @staticmethod
    def searchBySexo(model, texto, restricao):
        return model.select().where(model.nome.contains(texto)).where(model.sexo == restricao)

    @staticmethod
    def findByCpf(model, cpf):
        try:
            retorno= model.select().where(model.cpf == cpf).get()
        except DoesNotExist as e:
            return False
        else:
            return True

    @staticmethod
    def update(model, registros):
        id = registros['id']
        del registros['id']
        try:
            row = model.update(registros).where(model.id == id)
        except Exception as e:
            return e
        else:
            return row.execute()

    @staticmethod
    def delete(model, id):
        retorno = model.delete().where(model.id == id)
        return retorno.execute()

    @staticmethod
    def create(model, registros):
        try:
            row =  model.create(**registros)
        except Exception as e:
            return e
        else:
            return row

    @staticmethod
    def selectPerPage(model, page, number_for_page):
        return model.select().order_by(model.nome).paginate(page, number_for_page)