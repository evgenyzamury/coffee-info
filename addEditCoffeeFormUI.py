# Form implementation generated from reading ui file '.\addEditCoffeeForm.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 482)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(30, -1, 100, -1)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(40)
        self.gridLayout.setObjectName("gridLayout")
        self.roastEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.roastEdit.setObjectName("roastEdit")
        self.gridLayout.addWidget(self.roastEdit, 2, 1, 1, 1)
        self.molotEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.molotEdit.setObjectName("molotEdit")
        self.gridLayout.addWidget(self.molotEdit, 3, 1, 1, 1)
        self.descrEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.descrEdit.setObjectName("descrEdit")
        self.gridLayout.addWidget(self.descrEdit, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 7, 0, 2, 2)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.priceEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.priceEdit.setObjectName("priceEdit")
        self.gridLayout.addWidget(self.priceEdit, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 1, 1, 1, 1)
        self.VEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.VEdit.setObjectName("VEdit")
        self.gridLayout.addWidget(self.VEdit, 6, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 538, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Объём"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.label.setText(_translate("MainWindow", "Название сорта"))
        self.label_3.setText(_translate("MainWindow", "молотый/в зернах"))
        self.label_2.setText(_translate("MainWindow", "степень обжарки"))
        self.label_5.setText(_translate("MainWindow", "цена"))
        self.label_4.setText(_translate("MainWindow", "описание вкуса"))