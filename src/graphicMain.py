from Data import *
from __ProductManager import instance
from PyQt5.QtWidgets import *
from PIL import Image


class Graphic(QDialog):
    def __init__(self):
        super().__init__()
        self.__initUI()

    def __getCategory(self):
        """get category data"""
        self.category = []
        f = open('../res/data/category.txt', 'r') # TODO change DB

        for s in f.readlines():
            self.category.append(s)

    def moveSide(self, isLeft: bool):
        """moveSide(isLeft : boolean) -> None
        isLeft는 왼쪽 버튼 눌렀을 때 true"""
        # TODO go left or right widget
        pass

    def generateButton(self, product: Product):
        # TODO return Button
        raise NotImplemented('generateButton func in Graphic class')

    # product type별로 탭에 product 넣기.
    def __initUI(self):
        self.__getCategory()

        self.tabs = QTabWidget()

        for s in self.category:
            tab = QWidget()
            # TODO get product data to instance, and set on widget
            # TODO call generateButton
            self.tabs.addTab(tab, s)
