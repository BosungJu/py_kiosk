import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from __DBManager import instance

form_class = uic.loadUiType("kioskui.ui")[0]


def startUI():
    app = QApplication(sys.argv)
    window = GraphicMain()
    window.center()
    window.show()
    app.exec_()


class GraphicMain(QMainWindow, form_class):
    buttons = []
    mlist = []
    clist = []
    plist = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.stackTable.setCurrentIndex(0)
        self.orderMenu()
        self.addMenu()

        self.btn_order.clicked.connect(self.nextPage)
        self.btn_pay.clicked.connect(self.nextOrderPage)
        self.btn_pay2.clicked.connect(self.finishPage)
        self.btn_cancel.clicked.connect(self.clearOrder)
        self.btn_cancel2.clicked.connect(self.prePage)
        self.btn_back.clicked.connect(self.firstPage)

        self.tableWidget.setColumnWidth(0, 120)
        self.tableWidget.setColumnWidth(1, 110)
        self.tableWidget.setColumnWidth(2, 120)
        self.order_Count = 0
        self.total = 0

        # <editor-fold desc="button appending">
        self.buttons.append(self.menuBtn_1_1)
        self.buttons.append(self.menuBtn_1_2)
        self.buttons.append(self.menuBtn_1_3)
        self.buttons.append(self.menuBtn_1_4)
        self.buttons.append(self.menuBtn_1_5)
        self.buttons.append(self.menuBtn_2_1)
        self.buttons.append(self.menuBtn_2_2)
        self.buttons.append(self.menuBtn_2_3)
        self.buttons.append(self.menuBtn_2_4)
        self.buttons.append(self.menuBtn_2_5)
        self.buttons.append(self.menuBtn_3_1)
        self.buttons.append(self.menuBtn_3_2)
        self.buttons.append(self.menuBtn_3_3)
        self.buttons.append(self.menuBtn_3_4)
        self.buttons.append(self.menuBtn_3_5)
        self.buttons.append(self.menuBtn_3_6)
        self.buttons.append(self.menuBtn_3_7)
        self.buttons.append(self.menuBtn_4_1)
        self.buttons.append(self.menuBtn_4_2)
        self.buttons.append(self.menuBtn_4_3)
        self.buttons.append(self.menuBtn_4_4)
        self.buttons.append(self.menuBtn_4_5)
        self.buttons.append(self.menuBtn_4_6)
        self.buttons.append(self.menuBtn_4_7)
        self.buttons.append(self.menuBtn_4_8)
        # </editor-fold>

    def nextPage(self):
        page = self.stackTable.currentIndex()
        self.stackTable.setCurrentIndex(page + 1)

    def nextOrderPage(self):
        page = self.stackTable.currentIndex()
        if len(self.clist) == 0:
            self.stackTable.currentIndex()
        else:
            self.stackTable.setCurrentIndex(page + 1)
            self.orderPrint()

    def finishPage(self):
        page = self.stackTable.currentIndex()
        self.stackTable.setCurrentIndex(page + 1)
        self.orderCount()
        self.clearOrder()

    def prePage(self):
        page = self.stackTable.currentIndex()
        self.stackTable.setCurrentIndex(page - 1)

    def setFirstPage(self):
        page = self.stackTable.currentIndex()
        self.menuTap.setCurrentIndex(0)
        self.stackTable.setCurrentIndex(page - 3)

    def orderMenu(self):
        pcnt = 0
        products = instance.selectProduct(self)

        # 람다로 한 이유
        #
        for button in self.buttons:
            button.connect(lambda: self.buttonClickedEvent(name=products[pcnt].name, price=products[pcnt].price))
            pcnt += 1

    def buttonClickedEvent(self, name, price):
        if name in self.mlist:
            index = self.mlist.index(name)
            self.clist[index] += 1
            self.plist[index] = price * self.clist[index]
        else:
            self.mlist.append(name)
            self.clist.append(1)
            self.plist.append(price)
        self.addMenu()

    def orderPrint(self):
        for i in range(len(self.mlist)):
            self.tableWidget.setRowCount(len(self.mlist))
            self.tableWidget.setItem(i, 0, QTableWidgetItem(self.mlist[i]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(self.clist[i])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(self.plist[i])))
            self.total = sum(self.plist)
            self.text_total.setText(f"총 가격 : {self.total}원")

    def addMenu(self):
        self.text_mname.clear()
        self.text_count.clear()
        self.text_price.clear()
        for i in range(len(self.mlist)):
            self.text_mname.append(self.mlist[i])
            self.text_count.append(str(self.clist[i]))
            self.text_price.append(str(self.plist[i]))

    def clearOrder(self):
        self.mlist.clear()
        self.plist.clear()
        self.clist.clear()
        self.text_total.clear()
        self.text_mname.clear()
        self.text_price.clear()
        self.text_count.clear()
        self.total = 0

    def orderCount(self):
        self.order_Count += 1
        self.text_finish.append(f"대기 번호 {self.order_Count} 번")

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
