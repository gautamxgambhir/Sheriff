# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(929, 800)
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"../res/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(33, 33, 33, 255), stop:0.548023 rgba(15, 15, 15, 255));")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(340, 630, 271, 111))
        font1 = QFont()
        font1.setFamilies([u"Keep Calm"])
        font1.setPointSize(26)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: outset;\n"
"	border-radius: 15px;\n"
"	padding: 4px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(213, 213, 213);\n"
"}")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(180, 50, 581, 151))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 0, 151, 151))
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u"../res/logo.ico"))
        self.label.setScaledContents(True)
        self.label.setMargin(17)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 30, 521, 101))
        font2 = QFont()
        font2.setFamilies([u"Keep Calm"])
        font2.setPointSize(48)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color:rgb(51, 51, 51);")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(110, 430, 721, 111))
        font3 = QFont()
        font3.setFamilies([u"Keep Calm"])
        font3.setPointSize(36)
        self.textEdit.setFont(font3)
        self.textEdit.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
"border-radius:15px;\n"
"background-color:rgb(255,255,255);\n"
"}\n"
"QTextEdit:hover{\n"
"background-color:rgb(213, 213, 213);\n"
"}")
        self.textEdit.setAutoFormatting(QTextEdit.AutoAll)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 280, 591, 131))
        font4 = QFont()
        font4.setFamilies([u"Keep Calm"])
        font4.setPointSize(30)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"color:rgb(255,255,255);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sheriff - Home", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SHERIFF", None))
        self.textEdit.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ENTER SPEED LIMIT", None))
    # retranslateUi

