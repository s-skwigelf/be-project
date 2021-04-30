# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import cv2
import MySQLdb as mdb
#from qrui import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from bnk_options import Ui_bnkScrn

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 639)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 960, 640))
        self.frame_2.setStyleSheet("background-color: rgb(33, 170, 229);\n"
"background-color: rgb(173, 127, 168);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.topLabel = QtWidgets.QTextBrowser(self.frame_2)
        self.topLabel.setGeometry(QtCore.QRect(0, 0, 961, 111))
        self.topLabel.setStyleSheet("background-color: rgb(225, 255, 253);")
        self.topLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.topLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.topLabel.setLineWidth(3)
        self.topLabel.setObjectName("topLabel")
        self.welcomeText = QtWidgets.QTextBrowser(self.frame_2)
        self.welcomeText.setGeometry(QtCore.QRect(100, 200, 781, 221))
        self.welcomeText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.welcomeText.setObjectName("welcomeText")
        self.startBtn = QtWidgets.QPushButton(self.frame_2)
        self.startBtn.setGeometry(QtCore.QRect(160, 470, 651, 41))
        self.startBtn.setToolTip("")
        self.startBtn.setToolTipDuration(2)
        self.startBtn.setStyleSheet("background-color: rgb(224, 255, 253);")
        self.startBtn.setObjectName("startBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        self.startBtn.clicked.connect(self.DbConnect)
        #self.startBtn.clicked.connect(self.scan_read)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    #@pyqtSlot()
    def runSlot(self):
        pass
        #self.qrWindow()
        #self.tp()
        
    def tp(self):
        from bigrough import init_cam
        init_cam()
        self.MainWindow.hide()
        self.bnk_opsWindow()
        
    
    #@pyqtSlot()
    def bnk_opsWindow(self):
        #Dialog = QtWidgets.QDialog()
        #Dialog.uid = Ui_Dialog()
        #Dialog.uid.setupUi(Dialog)
        #Dialog.exec_()
        #Dialog.show()
        #Dialog.uid.startCam()
        
        bnkScrn = QtWidgets.QDialog()
        bnkScrn.ui = Ui_bnkScrn()
        bnkScrn.ui.setupUi(bnkScrn)
        bnkScrn.show()
        bnkScrn.exec_()
        
    def DbConnect(self):
        try:
            db = mdb.connect('localhost', 'root', '', 'atm')
            self.welcomeText.setText("DB connection successful")
        except mdb.Error as e:
            self.welcomeText.setText("DB connection failed")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.topLabel.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">ENHANCED ATM - For Cardless and Secure Transactions</span></p></body></html>"))
        self.welcomeText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">WELCOME</span></p></body></html>"))
        self.startBtn.setText(_translate("MainWindow", "Start"))

#import splash_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

