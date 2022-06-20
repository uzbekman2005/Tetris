from PyQt6.QtWidgets import QApplication, QMainWindow
from buttons import *
import sys

class Window(QMainWindow):
    def __init__(self,parent = None):
        super(Window, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn2.clicked.connect(self.twoPressed)
        self.ui.btn1.clicked.connect(self.onePressed)
        self.ui.btn3.clicked.connect(self.threePressed)
        self.ui.btn4.clicked.connect(self.fourPressed)

        self.hideOne()
        self.hideTwo()
        self.hideThree()
        self.hideFour()

    def twoPressed(self):
        # self.hideOne()
        self.hideOne()
        self.hideTwo()
        self.hideThree()
        self.hideFour()
        self.showTwo()

    def onePressed(self):
        self.hideOne()
        self.hideTwo()
        self.hideThree()
        self.hideFour()
        self.showOne()

    def threePressed(self):
        self.hideOne()
        self.hideTwo()
        self.hideThree()
        self.hideFour()
        self.showThree()

    def fourPressed(self):
        self.hideOne()
        self.hideTwo()
        self.hideThree()
        self.hideFour()
        self.showFour()

    def hideOne(self):
        self.ui.btnones1.hide()
        self.ui.btnones2.hide()
        self.ui.btnones3.hide()
        self.ui.btnones4.hide()

    def hideTwo(self):
        self.ui.btntwo1.hide()
        self.ui.btntwo2.hide()
        self.ui.btntwo3.hide()
        self.ui.btntwo4.hide()

    def hideThree(self):
        self.ui.btnthree1.hide()
        self.ui.btnthree2.hide()
        self.ui.btnthree3.hide()
        self.ui.btnthree4.hide()

    def hideFour(self):
        self.ui.btnfour1.hide()
        self.ui.btnfour2.hide()
        self.ui.btnfour3.hide()
        self.ui.btnfour4.hide()


    def showThree(self):
        self.ui.btnthree1.show()
        self.ui.btnthree2.show()
        self.ui.btnthree3.show()
        self.ui.btnthree4.show()

    def showOne(self):
        self.ui.btnones1.show()
        self.ui.btnones2.show()
        self.ui.btnones3.show()
        self.ui.btnones4.show()

    def showTwo(self):
        self.ui.btntwo1.show()
        self.ui.btntwo2.show()
        self.ui.btntwo3.show()
        self.ui.btntwo4.show()

    def showFour(self):
        self.ui.btnfour1.show()
        self.ui.btnfour2.show()
        self.ui.btnfour3.show()
        self.ui.btnfour4.show()

def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
