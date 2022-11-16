import requests
from Data import *

class __DBManager:
    # all functions use pass __sendQuery
    # ex) queryStr = f'select * from product where id={self.where}'
    # 다 선택하려면 where에 True로 넣기.
    # return __sendQuery(queryStr)

    url = 'http://127.0.0.1:8000/'

    def __dataProcessing(self, data, dataType):
        datas = []
        if dataType == "product":
            for d in data:
                pStr = d.split(' ')
                datas.append(Product(pStr[0], pStr[1], pStr[2], pStr[3]))
        else:
            for d in data:
                oStr = d.split(' ')
                datas.append(Order(int(oStr[0]), oStr[1], int(oStr[2]), oStr[3]))
        return datas

    def __sendQuery(self, queryStr, dataType):
        # TODO send query and get data
        url = self.url + '/' + dataType # ex) http://127.0.0.1:8000/product?data
        res = requests.post(url=url, data={'query': queryStr})
        data = res.json()['data'].split(';')
        return self.__dataProcessing(data, dataType)

    def selectProduct(self, where=True):
        if where:
            query = f'select * from product;'
        else:
            query = f'select * from product where pid={where};'

        query = 'product/' + query
        return self.__sendQuery(query, "product")


    def selectOrder(self, where=True): #오더 oid
        # TODO send select * from order where self.where
        if where:
            query = f'select * from porder;'
        else:
            query = f'select * from porder where pid={where};'

        query = 'porder/' + query
        return self.__sendQuery(query, "porder")

    def insertProduct(self, *dataSet):
        # TODO send insert into product values(dataSet...)
        query = 'insert into product values('
        for data in dataSet:
            query += data + ','

        query = str(query[:len(query) - 2]) + ');'
        query = 'Product/' + query
        return self.__sendQuery(query, "product")

    def insertOrder(self, *dataSet):
        # TODO send insert into order values(dataSet...)
        query = 'insert into porder values('
        for data in dataSet:
            query += data + ','

        query = str(query[:len(query) - 2]) + ');'
        query = 'porder/' + query
        return self.__sendQuery(query, "porder")

    def deleteProduct(self, where=True):
        # TODO send delete product where self.where
        if where:
            query = f'delete * from product;'
        else:
            query = f'delete * from product where pid={where};'

        query = 'product/' + query
        return self.__sendQuery(query, "product")

    def deleteOrder(self, where=True):
        # TODO send delete order where self.where
        if where:
            query = f'delete * from porder;'
        else:
            query = f'delete * from porder where pid={where};'

        query = 'porder/' + query
        return self.__sendQuery(query, "porder")

instance = __DBManager()