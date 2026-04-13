# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simulation.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.no_of_days = QSlider(self.centralwidget)
        self.no_of_days.setObjectName(u"no_of_days")
        self.no_of_days.setGeometry(QRect(20, 80, 160, 16))
        self.no_of_days.setMinimum(1)
        self.no_of_days.setMaximum(365)
        self.no_of_days.setSingleStep(5)
        self.no_of_days.setOrientation(Qt.Horizontal)
        self.initial = QSlider(self.centralwidget)
        self.initial.setObjectName(u"initial")
        self.initial.setGeometry(QRect(20, 110, 160, 16))
        self.initial.setMinimum(1000)
        self.initial.setMaximum(1000000)
        self.initial.setSingleStep(10000)
        self.initial.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 80, 61, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 110, 81, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 140, 61, 16))
        self.no_of_sims = QSlider(self.centralwidget)
        self.no_of_sims.setObjectName(u"no_of_sims")
        self.no_of_sims.setGeometry(QRect(20, 140, 160, 16))
        self.no_of_sims.setMinimum(1)
        self.no_of_sims.setMaximum(200)
        self.no_of_sims.setSingleStep(10)
        self.no_of_sims.setOrientation(Qt.Horizontal)
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(20, 190, 681, 391))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(280, 20, 281, 81))
        self.simulate_button = QPushButton(self.centralwidget)
        self.simulate_button.setObjectName(u"simulate_button")
        self.simulate_button.setGeometry(QRect(590, 30, 101, 51))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 30, 61, 16))
        self.comboBox_stock = QComboBox(self.centralwidget)
        self.comboBox_stock.setObjectName(u"comboBox_stock")
        self.comboBox_stock.setGeometry(QRect(80, 30, 121, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 18))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"No_of_Days", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Initial Amount", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"No_of_Sims", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.simulate_button.setText(QCoreApplication.translate("MainWindow", u"simulate", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Stock Name : ", None))
    # retranslateUi

