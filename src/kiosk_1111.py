import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("kioskui.ui")[0]


class Kiosk(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.mlist = []
        self.clist = []
        self.plist = []

        self.stackedWidget: QStackedWidget
        self.stackedWidget.setCurrentIndex(0)
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

    def nextPage(self):
        page = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(page + 1)

    def nextOrderPage(self):
        page = self.stackedWidget.currentIndex()
        if len(self.clist) == 0:
            self.stackedWidget.currentIndex()
        else:
            self.stackedWidget.setCurrentIndex(page + 1)
            self.orderPrint()

    def finishPage(self):
        page = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(page + 1)
        self.orderCount()
        self.clearOrder()

    def prePage(self):
        page = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(page - 1)

    def firstPage(self):
        page = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(page - 3)

    def orderMenu(self):
        self.menuBtn_1_1.clicked.connect(self.buttonClicked1)
        self.menuBtn_1_2.clicked.connect(self.buttonClicked2)
        self.menuBtn_1_3.clicked.connect(self.buttonClicked3)
        self.menuBtn_1_4.clicked.connect(self.buttonClicked4)
        self.menuBtn_2_1.clicked.connect(self.buttonClicked5)
        self.menuBtn_2_2.clicked.connect(self.buttonClicked6)
        self.menuBtn_2_3.clicked.connect(self.buttonClicked7)
        self.menuBtn_2_4.clicked.connect(self.buttonClicked8)
        self.menuBtn_3_1.clicked.connect(self.buttonClicked9)
        self.menuBtn_3_2.clicked.connect(self.buttonClicked10)

    def buttonClicked1(self):
        if "메뉴 1" in self.mlist:
            index = self.mlist.index("메뉴 1")
            self.clist[index] += 1
            self.plist[index] = 5000 * self.clist[index]
        else:
            self.mlist.append("메뉴 1")
            self.clist.append(1)
            self.plist.append(5000)
        self.addMenu()

    def buttonClicked2(self):
        if "메뉴 2" in self.mlist:
            index = self.mlist.index("메뉴 2")
            self.clist[index] += 1
            self.plist[index] = 5000 * self.clist[index]
        else:
            self.mlist.append("메뉴 2")
            self.clist.append(1)
            self.plist.append(5000)
        self.addMenu()

    def buttonClicked3(self):
        if "메뉴 3" in self.mlist:
            index = self.mlist.index("메뉴 3")
            self.clist[index] += 1
            self.plist[index] = 5000 * self.clist[index]
        else:
            self.mlist.append("메뉴 3")
            self.clist.append(1)
            self.plist.append(5000)
        self.addMenu()

    def buttonClicked4(self):
        if "메뉴 4" in self.mlist:
            index = self.mlist.index("메뉴 4")
            self.clist[index] += 1
            self.plist[index] = 5000 * self.clist[index]
        else:
            self.mlist.append("메뉴 4")
            self.clist.append(1)
            self.plist.append(5000)
        self.addMenu()

    def buttonClicked5(self):
        if "메뉴 5" in self.mlist:
            index = self.mlist.index("메뉴 5")
            self.clist[index] += 1
            self.plist[index] = 5000 * self.clist[index]
        else:
            self.mlist.append("메뉴 5")
            self.clist.append(1)
            self.plist.append(5000)
        self.addMenu()

    def buttonClicked6(self):
        if "메뉴 6" in self.mlist:
            index = self.mlist.index("메뉴 6")
            self.clist[index] += 1
            self.plist[index] = 5000 * self.clist[index]
        else:
            self.mlist.append("메뉴 6")
            self.clist.append(1)
            self.plist.append(5000)
        self.addMenu()

    def buttonClicked7(self):
        if "메뉴 7" in self.mlist:
            index = self.mlist.index("메뉴 7")
            self.clist[index] += 1
            self.plist[index] = 5000 * self.clist[index]
        else:
            self.mlist.append("메뉴 7")
            self.clist.append(1)
            self.plist.append(5000)
        self.addMenu()

    def buttonClicked8(self):
        if "메뉴 8" in self.mlist:
            index = self.mlist.index("메뉴 8")
            self.clist[index] += 1
            self.plist[index] = 5000 * self.clist[index]
        else:
            self.mlist.append("메뉴 8")
            self.clist.append(1)
            self.plist.append(5000)
        self.addMenu()

    def buttonClicked9(self):
        if "메뉴 9" in self.mlist:
            index = self.mlist.index("메뉴 9")
            self.clist[index] += 1
            self.plist[index] = 5000 * self.clist[index]
        else:
            self.mlist.append("메뉴 9")
            self.clist.append(1)
            self.plist.append(5000)
        self.addMenu()

    def buttonClicked10(self):
        if "메뉴 10" in self.mlist:
            index = self.mlist.index("메뉴 10")
            self.clist[index] += 1
            self.plist[index] = 5000 * self.clist[index]
        else:
            self.mlist.append("메뉴 10")
            self.clist.append(1)
            self.plist.append(5000)
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = Kiosk()
    Window.center()
    Window.show()
    app.exec_()
