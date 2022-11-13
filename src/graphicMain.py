import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("kioskUi.ui")[0]


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
        self.menuBtn_1_5.clicked.connect(self.buttonClicked5)
        self.menuBtn_2_1.clicked.connect(self.buttonClicked6)
        self.menuBtn_2_2.clicked.connect(self.buttonClicked7)
        self.menuBtn_2_3.clicked.connect(self.buttonClicked8)
        self.menuBtn_2_4.clicked.connect(self.buttonClicked9)
        self.menuBtn_2_5.clicked.connect(self.buttonClicked10)
        self.menuBtn_3_1.clicked.connect(self.buttonClicked11)
        self.menuBtn_3_2.clicked.connect(self.buttonClicked12)
        self.menuBtn_3_3.clicked.connect(self.buttonClicked13)
        self.menuBtn_3_4.clicked.connect(self.buttonClicked14)
        self.menuBtn_3_5.clicked.connect(self.buttonClicked15)
        self.menuBtn_3_6.clicked.connect(self.buttonClicked16)
        self.menuBtn_3_7.clicked.connect(self.buttonClicked17)
        self.menuBtn_4_1.clicked.connect(self.buttonClicked18)
        self.menuBtn_4_2.clicked.connect(self.buttonClicked19)
        self.menuBtn_4_3.clicked.connect(self.buttonClicked20)
        self.menuBtn_4_4.clicked.connect(self.buttonClicked21)
        self.menuBtn_4_5.clicked.connect(self.buttonClicked22)
        self.menuBtn_4_6.clicked.connect(self.buttonClicked23)
        self.menuBtn_4_7.clicked.connect(self.buttonClicked24)
        self.menuBtn_4_8.clicked.connect(self.buttonClicked25)

    def buttonClicked1(self):
        if "아메리카노" in self.mlist:
            index = self.mlist.index("아메리카노")
            self.clist[index] += 1
            self.plist[index] = 3500 * self.clist[index]
        else:
            self.mlist.append("아메리카노")
            self.clist.append(1)
            self.plist.append(3500)
        self.addMenu()

    def buttonClicked2(self):
        if "카라멜마끼아또" in self.mlist:
            index = self.mlist.index("카라멜마끼아또")
            self.clist[index] += 1
            self.plist[index] = 4000 * self.clist[index]
        else:
            self.mlist.append("카라멜마끼아또")
            self.clist.append(1)
            self.plist.append(4000)
        self.addMenu()

    def buttonClicked3(self):
        if "카페라떼" in self.mlist:
            index = self.mlist.index("카페라떼")
            self.clist[index] += 1
            self.plist[index] = 3500 * self.clist[index]
        else:
            self.mlist.append("카페라떼")
            self.clist.append(1)
            self.plist.append(3500)
        self.addMenu()

    def buttonClicked4(self):
        if "녹차라떼" in self.mlist:
            index = self.mlist.index("녹차라떼")
            self.clist[index] += 1
            self.plist[index] = 4000 * self.clist[index]
        else:
            self.mlist.append("녹차라떼")
            self.clist.append(1)
            self.plist.append(4000)
        self.addMenu()

    def buttonClicked5(self):
        if "초코라떼" in self.mlist:
            index = self.mlist.index("초코라떼")
            self.clist[index] += 1
            self.plist[index] = 4500 * self.clist[index]
        else:
            self.mlist.append("초코라떼")
            self.clist.append(1)
            self.plist.append(4500)
        self.addMenu()

    def buttonClicked6(self):
        if "요거트스무디" in self.mlist:
            index = self.mlist.index("요거트스무디")
            self.clist[index] += 1
            self.plist[index] = 5000 * self.clist[index]
        else:
            self.mlist.append("요거트스무디")
            self.clist.append(1)
            self.plist.append(5000)
        self.addMenu()

    def buttonClicked7(self):
        if "유자요거트스무디" in self.mlist:
            index = self.mlist.index("유자요거트스무디")
            self.clist[index] += 1
            self.plist[index] = 5200 * self.clist[index]
        else:
            self.mlist.append("유자요거트스무디")
            self.clist.append(1)
            self.plist.append(5200)
        self.addMenu()

    def buttonClicked8(self):
        if "피치요거트스무디" in self.mlist:
            index = self.mlist.index("피치요거트스무디")
            self.clist[index] += 1
            self.plist[index] = 5200 * self.clist[index]
        else:
            self.mlist.append("피치요거트스무디")
            self.clist.append(1)
            self.plist.append(5200)
        self.addMenu()

    def buttonClicked9(self):
        if "자바칩프라푸치노" in self.mlist:
            index = self.mlist.index("자바칩프라푸치노")
            self.clist[index] += 1
            self.plist[index] = 5500 * self.clist[index]
        else:
            self.mlist.append("자바칩프라푸치노")
            self.clist.append(1)
            self.plist.append(5500)
        self.addMenu()

    def buttonClicked10(self):
        if "그린티프라푸치노" in self.mlist:
            index = self.mlist.index("그린티프라푸치노")
            self.clist[index] += 1
            self.plist[index] = 5500 * self.clist[index]
        else:
            self.mlist.append("그린티프라푸치노")
            self.clist.append(1)
            self.plist.append(5500)
        self.addMenu()

    def buttonClicked11(self):
        if "라임에이드" in self.mlist:
            index = self.mlist.index("라임에이드")
            self.clist[index] += 1
            self.plist[index] = 3500 * self.clist[index]
        else:
            self.mlist.append("라임에이드")
            self.clist.append(1)
            self.plist.append(3500)
        self.addMenu()

    def buttonClicked12(self):
        if "자몽에이드" in self.mlist:
            index = self.mlist.index("자몽에이드")
            self.clist[index] += 1
            self.plist[index] = 3500 * self.clist[index]
        else:
            self.mlist.append("자몽에이드")
            self.clist.append(1)
            self.plist.append(3500)
        self.addMenu()

    def buttonClicked13(self):
        if "청포도에이드" in self.mlist:
            index = self.mlist.index("청포도에이드")
            self.clist[index] += 1
            self.plist[index] = 3700 * self.clist[index]
        else:
            self.mlist.append("청포도에이드")
            self.clist.append(1)
            self.plist.append(3700)
        self.addMenu()

    def buttonClicked14(self):
        if "홍차" in self.mlist:
            index = self.mlist.index("홍차")
            self.clist[index] += 1
            self.plist[index] = 3000 * self.clist[index]
        else:
            self.mlist.append("홍차")
            self.clist.append(1)
            self.plist.append(3000)
        self.addMenu()

    def buttonClicked15(self):
        if "녹차" in self.mlist:
            index = self.mlist.index("녹차")
            self.clist[index] += 1
            self.plist[index] = 3000 * self.clist[index]
        else:
            self.mlist.append("녹차")
            self.clist.append(1)
            self.plist.append(3000)
        self.addMenu()

    def buttonClicked16(self):
        if "자몽티" in self.mlist:
            index = self.mlist.index("자몽티")
            self.clist[index] += 1
            self.plist[index] = 3300 * self.clist[index]
        else:
            self.mlist.append("자몽티")
            self.clist.append(1)
            self.plist.append(3300)
        self.addMenu()

    def buttonClicked17(self):
        if "레몬티" in self.mlist:
            index = self.mlist.index("레몬티")
            self.clist[index] += 1
            self.plist[index] = 3300 * self.clist[index]
        else:
            self.mlist.append("레몬티")
            self.clist.append(1)
            self.plist.append(3300)
        self.addMenu()

    def buttonClicked18(self):
        if "레드벨벳케이크" in self.mlist:
            index = self.mlist.index("레드벨벳케이크")
            self.clist[index] += 1
            self.plist[index] = 6000 * self.clist[index]
        else:
            self.mlist.append("레드벨벳케이크")
            self.clist.append(1)
            self.plist.append(6000)
        self.addMenu()

    def buttonClicked19(self):
        if "치즈케이크" in self.mlist:
            index = self.mlist.index("치즈케이크")
            self.clist[index] += 1
            self.plist[index] = 6000 * self.clist[index]
        else:
            self.mlist.append("치즈케이크")
            self.clist.append(1)
            self.plist.append(6000)
        self.addMenu()

    def buttonClicked20(self):
        if "티라미수" in self.mlist:
            index = self.mlist.index("티라미수")
            self.clist[index] += 1
            self.plist[index] = 5500 * self.clist[index]
        else:
            self.mlist.append("티라미수")
            self.clist.append(1)
            self.plist.append(5500)
        self.addMenu()

    def buttonClicked21(self):
        if "에그타르트" in self.mlist:
            index = self.mlist.index("에그타르트")
            self.clist[index] += 1
            self.plist[index] = 4500 * self.clist[index]
        else:
            self.mlist.append("에그타르트")
            self.clist.append(1)
            self.plist.append(4500)
        self.addMenu()

    def buttonClicked22(self):
        if "모카스콘" in self.mlist:
            index = self.mlist.index("모카스콘")
            self.clist[index] += 1
            self.plist[index] = 3500 * self.clist[index]
        else:
            self.mlist.append("모카스콘")
            self.clist.append(1)
            self.plist.append(3500)
        self.addMenu()

    def buttonClicked23(self):
        if "스콘" in self.mlist:
            index = self.mlist.index("스콘")
            self.clist[index] += 1
            self.plist[index] = 3000 * self.clist[index]
        else:
            self.mlist.append("스콘")
            self.clist.append(1)
            self.plist.append(3000)
        self.addMenu()

    def buttonClicked24(self):
        if "마카롱" in self.mlist:
            index = self.mlist.index("마카롱")
            self.clist[index] += 1
            self.plist[index] = 3500 * self.clist[index]
        else:
            self.mlist.append("마카롱")
            self.clist.append(1)
            self.plist.append(3500)
        self.addMenu()

    def buttonClicked25(self):
        if "브라우니" in self.mlist:
            index = self.mlist.index("브라우니")
            self.clist[index] += 1
            self.plist[index] = 5000 * self.clist[index]
        else:
            self.mlist.append("브라우니")
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
