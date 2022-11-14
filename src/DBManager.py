import requests

class DBManager:
    # all functions use pass __sendQuery
    # ex) queryStr = f'select * from product where id={self.where}'
    # 다 선택하려면 where에 True로 넣기.
    # return __sendQuery(queryStr)

    url = 'http://127.0.0.1:8000/'


    def __sendQuery(self, queryStr):
        # TODO send query and get data
        requests.request(url=self.url + queryStr)
        return

    def selectProduct(self, where=True):
        if where:
            query = f'select * from product;'
        else:
            query = f'select * from product where id={where};'

        query = 'product/' + query
        return self.__sendQuery(query)


    def selectOrder(self, where=True):
        # TODO send select * from order where self.where
        return

    def insertProduct(self, dataSet):
        # TODO send insert into product values(dataSet...)
        return

    def insertOrder(self, dataSet):
        # TODO send insert into order values(dataSet...)
        return

    def deleteProduct(self, where=True):
        # TODO send delete product where self.where
        return

    def deleteOrder(self, where=True):
        # TODO send delete order where self.where
        return
