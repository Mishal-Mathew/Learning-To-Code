import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow ,QLabel,
                             QWidget ,QVBoxLayout,QHBoxLayout, QGridLayout,
                             QPushButton , QCheckBox , QRadioButton) #These are classes 
                             
from PyQt5.QtGui import QIcon ,QFont , QPixmap 
from PyQt5.QtCore import Qt     #For alignments

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.bg=input("Enter a colour: ")
        self.bg ="Red"

        self.setWindowTitle("Hello,new World!")
        self.setGeometry(700,300 , 1000 , 700)           #  ( x , y , width , height)
        self.setWindowIcon(QIcon("Legion.png"))
        
        self.label = QLabel("Hello, new World!",self)  # Construct a variable within the constructor as a good practice
        
        self.button_l = QPushButton("Click me to see layouts",self) 

        self.button = QPushButton("Click me!" , self)
        self.label_b = QLabel("Suprise Attack !",self)
        self.label_b2 = QLabel("😁",self)
        
        self.checkbox = QCheckBox("Yes",self)

        self.radiobutton1 = QRadioButton("Very Much",self)
        self.radiobutton2 = QRadioButton("Much",self)
        self.radiobutton3 = QRadioButton("Slightly",self)
        self.radiobutton4 = QRadioButton("Not even the slightest",self)


        self.labels()             # Do this to reduce load and put it into a function
        self.Images()
        self.initUI_buttons()
        self.initUI_checkbox()
        self.initUI_radio()

        
    def labels(self):
        
        self.label.setFont(QFont("Arial" , 30))          # ^ put self. before every label used because it is within the constructor
        self.label.setGeometry(0,0,self.width(),self.height())             #  else only label was needed no need of self.
        self.label.setStyleSheet(f"color: yellow; background-color:{self.bg}; font-weight: Bold; font-style: Italic; text-decoration: underline;")

        # Vertical Alignments
        
        #label.setAlignment(Qt.AlignTop)  
        #label.setAlignment(Qt.AlignBottom)
        #label.setAlignment(Qt.AlignVCenter)

        # Horizontal Alignments 

        #label.setAlignment(Qt.AlignRight)
        #label.setAlignment(Qt.AlignLeft)
        #label.setAlignment(Qt.AlignHCenter)

        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.label.setAlignment(Qt.AlignCenter)

    def Images(self):
        
        label = QLabel(self)                                          # ^ Else this 'label' and 'pixmap' will be local variable
        label.setGeometry(0,0, 150, 150)        # * This one right here!

        pixmap = QPixmap("Legion.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)

        label.setGeometry( (self.width() - label.width()) // 2 ,         # * self refers to the main window 
                           ((self.height() - label.height()) // 2) - 100,      #   label refers to the label mentioned above 
                           label.width() ,
                           label.height())

    def initUI(self):    #Initialize User - Interface
        Central_widget = QWidget()                   # ^ You got it by now right? 
        self.setCentralWidget(Central_widget)

        label1 = QLabel("Label 1",self)
        label2= QLabel("Label 2",self)
        label3 = QLabel("Label 3",self)
        label4= QLabel("Label 4",self)
        label5 = QLabel("Label 5",self)

        label1.setStyleSheet("background-color:red;")
        label2.setStyleSheet("background-color:yellow;")
        label3.setStyleSheet("background-color:blue;")
        label4.setStyleSheet("background-color:green;")
        label5.setStyleSheet("background-color:violet;")

        grid = QGridLayout()    # Can be QHBoxLayout or QVBoxLayout as well

        grid.addWidget(label1 , 0 , 0)
        grid.addWidget(label2 , 0 , 1)
        grid.addWidget(label3 , 1 , 0)
        grid.addWidget(label4 , 1 , 1)
        grid.addWidget(label5 , 2 , 2)

        Central_widget.setLayout(grid)

    def initUI_buttons(self):

        self.button.setGeometry(150,180 , 150 , 50)
        self.button.setStyleSheet("font-size: 30px; font-weight: Bold; font-style:Italic")
        self.button.setFont(QFont("Arial"))
        self.button.clicked.connect(self.on_click)

        self.button_l.setGeometry(10,100 , 500 , 50)
        self.button_l.setStyleSheet("font-size: 30px; font-weight: Bold; font-style:Italic")
        self.button_l.setFont(QFont("Arial"))
        self.button_l.clicked.connect(self.initUI)

        self.label_b2.setGeometry(0,400,self.width(),self.height())
        self.label_b2.setFont(QFont("Arial" , 70))
        self.label_b2.setAlignment(Qt.AlignHCenter)

        self.label_b.setStyleSheet(f"color:{self.bg};")

    def on_click(self):

        print("Button clicked!")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)


        self.label_b.setGeometry(0,-300,self.width(),self.height())
        self.label_b.setAlignment(Qt.AlignCenter)
        self.label_b.setStyleSheet("font-size: 100px; color: cyan; font-weight: Bold; font-style:Italic")

        self.label_b2.setStyleSheet("font-size: 50px; color: pink; font-weight: Bold; font-style:Italic")
        self.label_b2.setText("Did you get scared?")
        
    def initUI_checkbox(self):

        self.checkbox.setGeometry(350,450,150,150)
        self.checkbox.setStyleSheet("font-size: 30px; font-family: arial;")
        self.checkbox.stateChanged.connect(self.checked)
        self.checkbox.setChecked(False)

    def checked(self,state):

        # print(state)  if checked it's 2 else 0
        if state == Qt.Checked:
            print("Haha! Get scared")
        else:
            print("You didn't get scared?!")

    def initUI_radio(self):

        self.radiobutton1.setGeometry(0,0,150,150)
        self.radiobutton2.setGeometry(0,0,150,150)
        self.radiobutton3.setGeometry(0,0,150,150)
        self.radiobutton4.setGeometry(0,0,150,150)

        self.setStyleSheet({QRadioButton ("font-size: 30px;")})


def main():
    app = QApplication(sys.argv)    # app and window are objects of the class
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()