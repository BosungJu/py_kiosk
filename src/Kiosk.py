import Data

class Kiosk:
    def __init__(self):
        self.productPath = ''
        self.order = Data.Order()
        self.products = []


    # data format
    # productName,productPrice
    def asyncProduct(self):
        f = open(self.productPath, 'r')

        pData = f.readlines()

        for data in pData:
            pName = data.split()[0]
            pPrice = data.split()[1]
            self.products.append(Data.Product(pName[0], pPrice[1]))

    def updateProduct(self):
        #TODO update product
        raise NotImplemented('update product func in Kiosk class.')
