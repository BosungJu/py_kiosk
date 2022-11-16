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
        self.orderList = productIds  # Product[]
        self.price = price  # int

        if date == '':
            self.date = datetime.now().strftime('%Y-%M-%D/%H:%M:%S')
        else:
            self.date = date

    def addOrder(self, product: Product):
        """addOrder(product : Product) -> None"""
        if product is not Product:
            raise AttributeError('addOrder product is not Product.')

        self.orderList += f'{product.id} '
        self.price += product.price

    def clearOrder(self):
        """deleteOrder(index : int)
        delete from Order"""
        self.orderList = ''
        self.price = 0

    def toString(self):
        return f'{self.id} {self.date} {self.price} {self.orderList}'