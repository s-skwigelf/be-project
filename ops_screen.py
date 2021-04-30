# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ops_screen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ops_Scrn(object):
    def setupUi(self, ops_Scrn):
        ops_Scrn.setObjectName("ops_Scrn")
        ops_Scrn.resize(960, 640)
        ops_Scrn.setStyleSheet("background-color: rgb(33, 170, 229);\n"
"background-color: rgb(173, 127, 168);")
        ops_Scrn.setModal(False)
        self.topLabel = QtWidgets.QTextBrowser(ops_Scrn)
        self.topLabel.setGeometry(QtCore.QRect(0, 0, 961, 111))
        self.topLabel.setStyleSheet("background-color: rgb(225, 255, 253);")
        self.topLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.topLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.topLabel.setLineWidth(3)
        self.topLabel.setObjectName("topLabel")
        self.QRframe = QtWidgets.QLabel(ops_Scrn)
        self.QRframe.setGeometry(QtCore.QRect(20, 130, 921, 491))
        self.QRframe.setFrameShape(QtWidgets.QFrame.Panel)
        self.QRframe.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.QRframe.setLineWidth(3)
        self.QRframe.setText("")
        self.QRframe.setObjectName("QRframe")
        self.verticalWidget_2 = QtWidgets.QWidget(ops_Scrn)
        self.verticalWidget_2.setGeometry(QtCore.QRect(500, 250, 431, 241))
        self.verticalWidget_2.setStyleSheet("gridline-color: rgb(255, 255, 255);")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.msBtn = QtWidgets.QPushButton(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msBtn.sizePolicy().hasHeightForWidth())
        self.msBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.msBtn.setFont(font)
        self.msBtn.setAutoFillBackground(False)
        self.msBtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(166, 166, 166);\n"
"selection-color: rgb(170, 255, 255);")
        self.msBtn.setObjectName("msBtn")
        self.verticalLayout_2.addWidget(self.msBtn)
        self.wdBtn_2 = QtWidgets.QPushButton(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wdBtn_2.sizePolicy().hasHeightForWidth())
        self.wdBtn_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wdBtn_2.setFont(font)
        self.wdBtn_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(166, 166, 166);\n"
"selection-color: rgb(170, 255, 255);")
        self.wdBtn_2.setObjectName("wdBtn_2")
        self.verticalLayout_2.addWidget(self.wdBtn_2)
        self.verticalWidget = QtWidgets.QWidget(ops_Scrn)
        self.verticalWidget.setGeometry(QtCore.QRect(30, 250, 431, 241))
        self.verticalWidget.setAutoFillBackground(False)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wdBtn = QtWidgets.QPushButton(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wdBtn.sizePolicy().hasHeightForWidth())
        self.wdBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wdBtn.setFont(font)
        self.wdBtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(166, 166, 166);\n"
"selection-color: rgb(170, 255, 255);")
        self.wdBtn.setObjectName("wdBtn")
        self.verticalLayout.addWidget(self.wdBtn)
        self.beBtn = QtWidgets.QPushButton(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.beBtn.sizePolicy().hasHeightForWidth())
        self.beBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.beBtn.setFont(font)
        self.beBtn.setAutoFillBackground(False)
        self.beBtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(166, 166, 166);\n"
"selection-color: rgb(170, 255, 255);")
        self.beBtn.setObjectName("beBtn")
        self.verticalLayout.addWidget(self.beBtn)

        self.retranslateUi(ops_Scrn)
        QtCore.QMetaObject.connectSlotsByName(ops_Scrn)

    def retranslateUi(self, ops_Scrn):
        _translate = QtCore.QCoreApplication.translate
        ops_Scrn.setWindowTitle(_translate("ops_Scrn", "Dialog"))
        self.topLabel.setHtml(_translate("ops_Scrn", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">ENHANCED ATM - For Cardless and Secure Transactions</span></p></body></html>"))
        self.msBtn.setText(_translate("ops_Scrn", "Mini statement"))
        self.wdBtn_2.setText(_translate("ops_Scrn", "Another function"))
        self.wdBtn.setText(_translate("ops_Scrn", "Withdraw"))
        self.beBtn.setText(_translate("ops_Scrn", "Balance enquiry"))

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ops_Scrn = QtWidgets.QDialog()
    ui = Ui_ops_Scrn()
    ui.setupUi(ops_Scrn)
    ops_Scrn.show()
    sys.exit(app.exec_())
"""
