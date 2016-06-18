# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1083, 532)
        Form.setWindowOpacity(1.0)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        #Form.setStyleSheet("background-color: red;");
        #Trades table
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(50, 30, 991, 411))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        
        #All, Open, Closed radio buttons.
        self.radioButton = QtGui.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 31, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 50, 31, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 66, 31, 21))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        
        #Add button
        self.addBtn = QtGui.QPushButton(Form)
        self.addBtn.setGeometry(QtCore.QRect(940, 450, 101, 41))
        
        
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Malgun Gothic Semilight"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.addBtn.setFont(font)
        self.addBtn.setObjectName(_fromUtf8("addBtn"))
        
        #Statistic table
        self.tableWidget2 = QtGui.QTableWidget(Form)
        self.tableWidget2.setGeometry(QtCore.QRect(50, 450, 881, 61))
        self.tableWidget2.setObjectName(_fromUtf8("tableWidget"))
        
        #Save/refresh button
        self.saveBtn = QtGui.QPushButton(Form)
        self.saveBtn.setGeometry(QtCore.QRect(940, 490, 101, 23))
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))
        
        #File name label
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(450, 10, 900, 20))
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        
        self.tableWidget.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.addBtn.raise_()
        self.tableWidget2.raise_()
        self.radioButton_3.raise_()
        self.saveBtn.raise_()
        self.label.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Trade journal", None))
        self.radioButton.setText(_translate("Form", "A", None))
        self.radioButton_2.setText(_translate("Form", "O", None))
        self.radioButton_3.setText(_translate("Form", "C", None))
        self.addBtn.setText(_translate("Form", "Add", None))
        self.saveBtn.setText(_translate("Form", "Save/Refresh", None))
        self.label.setText(_translate("Form", "Table", None))


