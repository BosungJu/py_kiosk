# import DB

class DBManager:
    # all functions use pass __sendQuery
    # ex) queryStr = f'select * from product where id={self.where}'
    # 다 선택하려면 where에 True로 넣기.
    # return __sendQuery(queryStr)
    def __sendQuery(self, queryStr):
        # TODO send query and get data
        return

    def selectProduct(self, where='*'):
        if where:
            query = f'select * from product;'
        else:
            query = f'select * from product where id={where};'

        return self.__sendQuery(query)


    def selectOrder(self, where='*'):
        # TODO send select * from order where self.where
        return

    def insertProduct(self, dataSet):
        # TODO send insert into product values(dataSet...)
        return

    def insertOrder(self, dataSet):
        # TODO send insert into order values(dataSet...)
        return

    def deleteProduct(self, where='*'):
        # TODO send delete product where self.where
        return

    def deleteOrder(self, where='*'):
        # TODO send delete order where self.where
        return
