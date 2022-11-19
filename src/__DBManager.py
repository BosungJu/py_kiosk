import requests
from Data import *

class __DBManager:
    # all functions use pass __sendQuery
    # ex) queryStr = f'select * from product where id={self.where}'
    # 다 선택하려면 where에 True로 넣기.
    # return __sendQuery(queryStr)

    url = 'http://127.0.0.1:5000'

    def __dataProcessing(self, data, dataType):
        datas = []

        if dataType == "product":
            for d in data:
                datas.append(Product(int(d['id']), d['name'], int(d['price']), d['category']))
        else:
            for d in data:
                datas.append(Order(int(d['id']), d['date'], int(d['price']), d['products']))
        print(datas)

        return datas

    def __sendQuery(self, query):
        # TODO send query and get data
        url = self.url + '/query' # ex) http://127.0.0.1:5000/product?data
        res = requests.get(url=url, params=query)
        print(res)

        if res.status_code != 200:
            print('error')
            return []

        data = res.json()
        print(data)
        res.close()
        return self.__dataProcessing(data, query['tableName'])

    def selectProduct(self, where=True):
        if where:
            query = {'queryType': 'select', 'params': '*', 'tableName': 'product', 'data': ''}
        else:
            query = {'queryType': 'select', 'params': '*', 'tableName': 'product', 'data': where}

        return self.__sendQuery(query)

    def selectOrder(self, where=True): #오더 oid
        # TODO send select * from order where self.where
        if where:
            query = {'queryType': 'select', 'params': '*', 'tableName': 'porder', 'data': ''}
        else:
            query = {'queryType': 'select', 'params': '*', 'tableName': 'porder', 'data': where}

        return self.__sendQuery(query)

    def insertProduct(self, *dataSet):
        # TODO send insert into product values(dataSet...)
        query = {'queryType': 'insert', 'tableName': 'product', 'datas': dataSet}
        return self.__sendQuery(query)

    def insertOrder(self, *dataSet):
        # TODO send insert into order values(dataSet...)
        query = {'queryType': 'insert', 'tableName': 'porder', 'datas': dataSet}
        return self.__sendQuery(query)

    def deleteProduct(self, where=True):
        # TODO send delete product where self.where
        query = {'queryType': 'delete', 'tableName': 'product', 'data': where}
        return self.__sendQuery(query)

    def deleteOrder(self, where=True):
        # TODO send delete order where self.where
        query = {'queryType': 'delete', 'tableName': 'porder', 'data': where}
        return self.__sendQuery(query)

instance = __DBManager()