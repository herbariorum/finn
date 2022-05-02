from peewee import DoesNotExist

class ResponsavelDataSet:

    @staticmethod
    def selectAll(model):
        return model.select()

    @staticmethod
    def selectById(model, id):
        return model.select().where(model.id == id)