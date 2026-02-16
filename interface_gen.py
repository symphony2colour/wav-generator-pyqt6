from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(345, 506)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        
        self.lineOne = QtWidgets.QLineEdit(self.centralwidget)
        self.lineOne.setObjectName("Line1")
        self.verticalLayout.addWidget(self.lineOne)

        self.lineTwo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineTwo.setObjectName("Line2")
        self.verticalLayout.addWidget(self.lineTwo)

        self.lineThree = QtWidgets.QLineEdit(self.centralwidget)
        self.lineThree.setObjectName("Line3")
        self.verticalLayout.addWidget(self.lineThree)
        
        self.lineFour = QtWidgets.QLineEdit(self.centralwidget)
        self.lineFour.setObjectName("Line4")
        self.verticalLayout.addWidget(self.lineFour)

        self.lineFive = QtWidgets.QLineEdit(self.centralwidget)
        self.lineFive.setObjectName("Line5")
        self.verticalLayout.addWidget(self.lineFive)
        
        
        self.btnBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowse2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowse.setObjectName("btnBrowse")
        self.btnBrowse2.setObjectName("btnBrowse2")
        self.verticalLayout.addWidget(self.btnBrowse)
        self.verticalLayout.addWidget(self.btnBrowse2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wav Gen"))
        self.btnBrowse.setText(_translate("MainWindow", "Chose directory"))
        self.btnBrowse2.setText(_translate("MainWindow", "Generate WAV"))
        self.lineOne.setText(_translate("MainWindow", "SAMPLE RATE (Example: 44100)"))
        self.lineTwo.setText(_translate("MainWindow", "NUMBER OF SECONDS (Must be > 0)"))
        self.lineThree.setText(_translate("MainWindow", "FREQUENCY IN HZ (range 1...20000Hz)"))
        self.lineFour.setText(_translate("MainWindow", "VOLUME (Float value between 1.0 and 10.0)"))
        self.lineFive.setText(_translate("MainWindow", "Filename"))
        


