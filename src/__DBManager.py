import requests
from Data import *

class __DBManager:
    # all functions use pass __sendQuery
    # ex) queryStr = f'select * from product where id={self.where}'
    # 다 선택하려면 where에 True로 넣기.
    # return __sendQuery(queryStr)

    url = 'http://127.0.0.1:5000/'

    def __dataProcessing(self, data, dataType):
        datas = []

        if data[0].get('what') is not None:
            return []

        if dataType == "product":
            for d in data:
                datas.append(Product(int(d['id']), d['name'], int(d['price']), d['category']))
        else:
            for d in data:
                datas.append(Order(int(d['id']), d['date'], int(d['price']), d['products']))

        return datas

    def __sendQuery(self, query):
        # TODO send query and get data
        url = self.url # ex) http://127.0.0.1:5000/?query
        res = requests.get(url=url, params=query)
        print(res)

        if res.status_code != 200: # error가 나오는 경우는 데이터가 없는 경우 밖에 없음.
            print('error', end=' ')
            print(query['queryType'], end=' ')
            print(query['tableName'])
            data = []
        else:
            data = res.json()
        res.close()
        return self.__dataProcessing(data, query['tableName'])

    def selectProduct(self, where=True):
        if where:
            query = {'queryType': 'select', 'params': '*', 'tableName': 'product', 'data': ''}
        else:
            query = {'queryType': 'select', 'params': '*', 'tableName': 'product', 'data': where}

        return self.__sendQuery(query)

    def selectOrder(self, where=True):
        if where:
            query = {'queryType': 'select', 'params': '*', 'tableName': 'porder', 'data': ''}
        else:
            query = {'queryType': 'select', 'params': '*', 'tableName': 'porder', 'data': where}

        return self.__sendQuery(query)

    def insertProduct(self, datas):
        query = {'queryType': 'insert', 'tableName': 'product', 'datas': datas}
        return self.__sendQuery(query)

    def insertOrder(self, datas):
        query = {'queryType': 'insert', 'tableName': 'porder', 'datas': datas}
        return self.__sendQuery(query)

    def deleteProduct(self, where=True):
        query = {'queryType': 'delete', 'tableName': 'product', 'data': where}
        return self.__sendQuery(query)

    def deleteOrder(self, where=True):
        query = {'queryType': 'delete', 'tableName': 'porder', 'data': where}
        return self.__sendQuery(query)

instance = __DBManager()