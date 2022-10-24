
class Product:
    def __init__(self, name : str, price : int, _type : str):
        '''__init__(name : str, price : int, _type : str)'''
        self.name = name
        self.price = price
        self.type = _type


class Order:
    def __init__(self):
        self.undoList = [] # 저장 안함
        self.orderList = [] # Product[]
        self.price = 0 # int

    def addOrder(self, product: Product):
        '''addOrder(product : Product) -> None'''
        if product is not Product:
            raise AttributeError('addOrder product is not Product.')

        self.undoList.append((self.orderList, self.price))

        self.orderList.append(product)
        self.price += product.price

    def deleteOrder(self, index: int):
        '''deleteOrder(index : int)
        delete from Order'''
        self.undoList.append((self.orderList, self.price))
        self.price -= self.orderList[index].price
        self.orderList.remove(self.orderList[index])

    def undo(self):
        '''previous behavior cancel'''
        if len(self.undoList) == 0:
            raise IndexError('length of the undoList is 0.')

        undoData = self.undoList.pop()
        self.orderList, self.price = undoData

    def saveOrder(self):
        '''order data save to ../res/data/order.txt'''
        # TODO save order.txt
        raise NotImplemented()
