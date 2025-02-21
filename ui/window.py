# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(748, 577)
        MainWindow.setStyleSheet("* {\n"
"    font: 20pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(0, 170, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageMenu = QtWidgets.QWidget()
        self.pageMenu.setObjectName("pageMenu")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.pageMenu)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(parent=self.pageMenu)
        self.frame_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelUsername = QtWidgets.QLabel(parent=self.frame_2)
        self.labelUsername.setMinimumSize(QtCore.QSize(0, 50))
        self.labelUsername.setObjectName("labelUsername")
        self.verticalLayout_4.addWidget(self.labelUsername, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frameMenuBtns = QtWidgets.QFrame(parent=self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameMenuBtns.sizePolicy().hasHeightForWidth())
        self.frameMenuBtns.setSizePolicy(sizePolicy)
        self.frameMenuBtns.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameMenuBtns.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameMenuBtns.setObjectName("frameMenuBtns")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frameMenuBtns)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btnLow = QtWidgets.QPushButton(parent=self.frameMenuBtns)
        self.btnLow.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnLow.setFont(font)
        self.btnLow.setObjectName("btnLow")
        self.verticalLayout_6.addWidget(self.btnLow)
        self.btnMedium = QtWidgets.QPushButton(parent=self.frameMenuBtns)
        self.btnMedium.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnMedium.setFont(font)
        self.btnMedium.setObjectName("btnMedium")
        self.verticalLayout_6.addWidget(self.btnMedium)
        self.btnHard = QtWidgets.QPushButton(parent=self.frameMenuBtns)
        self.btnHard.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnHard.setFont(font)
        self.btnHard.setObjectName("btnHard")
        self.verticalLayout_6.addWidget(self.btnHard)
        self.btnExit = QtWidgets.QPushButton(parent=self.frameMenuBtns)
        self.btnExit.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnExit.setFont(font)
        self.btnExit.setObjectName("btnExit")
        self.verticalLayout_6.addWidget(self.btnExit)
        self.verticalLayout_4.addWidget(self.frameMenuBtns)
        self.horizontalLayout.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.pageMenu)
        self.pageLogin = QtWidgets.QWidget()
        self.pageLogin.setObjectName("pageLogin")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.pageLogin)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(parent=self.pageLogin)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.editLogin = QtWidgets.QLineEdit(parent=self.frame)
        self.editLogin.setMinimumSize(QtCore.QSize(200, 50))
        self.editLogin.setMaximumSize(QtCore.QSize(200, 50))
        self.editLogin.setText("")
        self.editLogin.setObjectName("editLogin")
        self.verticalLayout_2.addWidget(self.editLogin, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.btnLogin = QtWidgets.QPushButton(parent=self.frame)
        self.btnLogin.setMinimumSize(QtCore.QSize(200, 50))
        self.btnLogin.setMaximumSize(QtCore.QSize(200, 50))
        self.btnLogin.setObjectName("btnLogin")
        self.verticalLayout_2.addWidget(self.btnLogin, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_3.addWidget(self.frame, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.stackedWidget.addWidget(self.pageLogin)
        self.pageEnd = QtWidgets.QWidget()
        self.pageEnd.setObjectName("pageEnd")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.pageEnd)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(parent=self.pageEnd)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(parent=self.frame_3)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.btnMenu = QtWidgets.QPushButton(parent=self.frame_3)
        self.btnMenu.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnMenu.setFont(font)
        self.btnMenu.setObjectName("btnMenu")
        self.verticalLayout_5.addWidget(self.btnMenu, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.pageEnd)
        self.page_counter = QtWidgets.QWidget()
        self.page_counter.setObjectName("page_counter")
        self.count = QtWidgets.QLCDNumber(parent=self.page_counter)
        self.count.setGeometry(QtCore.QRect(560, 100, 131, 51))
        self.count.setObjectName("count")
        self.label_2 = QtWidgets.QLabel(parent=self.page_counter)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 561, 121))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page_counter)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelUsername.setText(_translate("MainWindow", "TextLabel"))
        self.btnLow.setText(_translate("MainWindow", "low"))
        self.btnMedium.setText(_translate("MainWindow", "medium"))
        self.btnHard.setText(_translate("MainWindow", "hard"))
        self.btnExit.setText(_translate("MainWindow", "Exit"))
        self.editLogin.setPlaceholderText(_translate("MainWindow", "Введите Ваш никнейм"))
        self.btnLogin.setText(_translate("MainWindow", "Готово"))
        self.label.setText(_translate("MainWindow", "End Game! Your score: 1000 "))
        self.btnMenu.setText(_translate("MainWindow", "Menu"))
        self.label_2.setText(_translate("MainWindow", "Количество съеденных яблочек:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
