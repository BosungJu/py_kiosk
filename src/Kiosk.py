from Data import Order
from graphicMain import GraphicMain
from __ProductManager import instance

class Kiosk:
    graphic = GraphicMain()

    def __init__(self):
        # TODO start Kiosk
        self.graphic.startUI()
        return

    def updateProduct(self):
        # TODO update product
        raise NotImplemented('update product func in Kiosk class.')
