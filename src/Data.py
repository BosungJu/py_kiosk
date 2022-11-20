from datetime import datetime

class Product:
    def __init__(self, id: int, name: str, price: int, categoty:str=''):
        """__init__(id : int, name : str, price : int, _type : str)"""
        self.id = id
        self.name = name
        self.price = price
        self.category = categoty

    def toString(self):
        return f'{self.id} {self.name} {self.price} {self.category}'


class Order:
    def __init__(self, id: int, productIds: str= '', price: int=0, date: str= ''):
        self.id = id
        self.products = productIds  # Product[]
        self.price = price  # int

        if date == '':
            self.date = 'current_timestamp()'
        else:
            self.date = date

    def addOrder(self, product: Product):
        """addOrder(product : Product) -> None"""
        if type(product).__name__ != 'Product':
            raise AttributeError('addOrder product is not Product.')

        self.products += f'{product.id} '
        self.price += product.price

    def clearOrder(self):
        """deleteOrder(index : int)
        delete from Order"""
        self.products = ''
        self.price = 0

    def toString(self):
        return f'{self.id}, {self.date}, {self.price}, {self.products}'

    def toValues(self):
        return f'{self.id}, {self.date}, {self.price}, "{self.products}", NULL'