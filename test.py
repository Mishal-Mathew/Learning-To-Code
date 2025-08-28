import sys
from PyQt5.QtWidgets import QApplication , QMainWindow ,QPushButton
from PyQt5.QtGui import QIcon

class M_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Testing window")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("Legion.png"))
        self.initUI()

    def initUI(self):

        button = QPushButton("Click me!" , self)
        button.setGeometry(150 ,200 ,150 ,150)
        button.setStyleSheet("font-size: 30px")


def main():
    app = QApplication(sys.argv)
    window = M_window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()