from ProductManager import instance
from PyQt5.QtWidgets import *

class Graphic(QDialog):
    def __init__(self):
        super().__init__()

    # product data 받고 type별로 정보 가공
    def getProductData(self):
        products = instance.getData()

        for product in products.values():
            if product.type:
                pass

    # product type별로 탭에 product 넣기.
    def initUI(self):
        tab = QTabWidget()
        self.tabs = []