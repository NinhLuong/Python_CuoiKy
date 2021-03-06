# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_splash_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc1

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(483, 451)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 461, 431))
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 231, 430))
        self.frame.setStyleSheet("border-image: url(:/images/images/images/khoidong.png);\n"
"border-top-left-radius: 50px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setGeometry(QtCore.QRect(230, 0, 231, 430))
        self.frame_2.setStyleSheet("background-image: url(:/images/images/images/5172658.jpg);\n"
"border-bottom-right-radius: 50px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.circularProgressBarBase = QtWidgets.QFrame(self.frame_2)
        self.circularProgressBarBase.setGeometry(QtCore.QRect(20, 130, 181, 181))
        self.circularProgressBarBase.setStyleSheet("background: none;\n"
"border-radius: 90px;\n"
"background-color: rgb(0, 0, 127);\n"
"")
        self.circularProgressBarBase.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBarBase.setObjectName("circularProgressBarBase")
        self.circulBg = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circulBg.setGeometry(QtCore.QRect(0, 0, 181, 181))
        self.circulBg.setStyleSheet("QFrame{\n"
"    border-radius: 90px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.748 rgba(255, 0, 255, 0), stop:0.749 rgba(241, 0, 120, 255));\n"
"}")
        self.circulBg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circulBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circulBg.setObjectName("circulBg")
        self.circulProgress = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circulProgress.setGeometry(QtCore.QRect(10, 10, 161, 161))
        self.circulProgress.setStyleSheet("QFrame{\n"
"    border-radius: 80px;\n"
"    background-color: rgb(77,77, 127);\n"
"}")
        self.circulProgress.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circulProgress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circulProgress.setObjectName("circulProgress")
        self.container = QtWidgets.QFrame(self.circularProgressBarBase)
        self.container.setEnabled(True)
        self.container.setGeometry(QtCore.QRect(30, 40, 121, 101))
        self.container.setStyleSheet("QFrame{\n"
"    border-radius: 130px;\n"
"    background-color: rgb(77,77, 127);\n"
"}")
        self.container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.labelPercentage = QtWidgets.QLabel(self.container)
        self.labelPercentage.setGeometry(QtCore.QRect(10, 10, 121, 41))
        self.labelPercentage.setStyleSheet("QFrame{\n"
"            border-radius: 150px;\n"
"            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));\n"
"        }")
        self.labelPercentage.setObjectName("labelPercentage")
        self.labelLoadingInfo = QtWidgets.QLabel(self.container)
        self.labelLoadingInfo.setGeometry(QtCore.QRect(10, 80, 101, 20))
        self.labelLoadingInfo.setStyleSheet("font: 8pt \"Microsoft JhengHei\";\n"
"background-color: rgb(112, 112, 167);\n"
"border-radius: 10px;\n"
"")
        self.labelLoadingInfo.setObjectName("labelLoadingInfo")
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.labelPercentage.setText(_translate("SplashScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">0</span><span style=\" font-size:20pt; font-weight:600; color:#ffffff; vertical-align:super;\">%</span></p></body></html>"))
        self.labelLoadingInfo.setText(_translate("SplashScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:600; color:#ffffff;\">loading...</span></p></body></html>"))

