from reportlab.platypus import Flowable


class MCLine(Flowable):

    def __init__(self, width, height=0):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    def __repr__(self):
        return "Line {}".format(self.width)

    def draw(self):
        self.canv.line(10, self.height, self.width, self.height)

