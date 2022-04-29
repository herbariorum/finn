from peewee import DoesNotExist

class ResponsavelDataSet:

    @staticmethod
    def selectAll(model):
        return model.select()