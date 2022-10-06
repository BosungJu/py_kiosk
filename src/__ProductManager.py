from Data import *
import pickle

class __ProductManager():
    def __init__(self):
        self.f = open('../res/product.txt', 'rb')
        self.products = {}
        self.__loadData()

    def __loadData(self):
        while self.f is not None:
            temp = pickle.load(self.f)
            self.products[temp.name] = temp

    def addData(self, product):
        self.products[product.name] = product

    def deleteData(self, product):
        self.products.pop(product.name)

    def saveData(self):
        self.f = open('../res/product.txt', 'wb')

        for data in self.products:
            pickle.dump(data, self.f)

    def getData(self):
        return self.products

    def getDataToList(self):
        return list(self.products.values())


instance = __ProductManager()