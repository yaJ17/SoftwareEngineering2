# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainOWiOGh.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(908, 457)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logo_wannabe = QLabel(self.centralwidget)
        self.logo_wannabe.setObjectName(u"logo_wannabe")
        self.logo_wannabe.setGeometry(QRect(20, 30, 181, 31))
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(14)
        font.setBold(True)
        self.logo_wannabe.setFont(font)
        self.logo_wannabe.setTextFormat(Qt.TextFormat.AutoText)
        self.menu_label = QLabel(self.centralwidget)
        self.menu_label.setObjectName(u"menu_label")
        self.menu_label.setGeometry(QRect(20, 70, 181, 31))
        self.menu_label.setFont(font)
        self.menu_label.setTextFormat(Qt.TextFormat.AutoText)
        self.search_label = QLabel(self.centralwidget)
        self.search_label.setObjectName(u"search_label")
        self.search_label.setGeometry(QRect(341, 20, 91, 51))
        self.search_label.setFont(font)
        self.search_label.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.search_label.setTextFormat(Qt.TextFormat.AutoText)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(220, 20, 20, 631))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.search_bar = QLineEdit(self.centralwidget)
        self.search_bar.setObjectName(u"search_bar")
        self.search_bar.setGeometry(QRect(440, 30, 241, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.search_bar.setFont(font1)
        self.search_bar.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.dashboard_label = QLabel(self.centralwidget)
        self.dashboard_label.setObjectName(u"dashboard_label")
        self.dashboard_label.setGeometry(QRect(250, 20, 91, 51))
        self.dashboard_label.setFont(font)
        self.dashboard_label.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.dashboard_label.setTextFormat(Qt.TextFormat.AutoText)
        self.username = QLabel(self.centralwidget)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(710, 20, 161, 51))
        self.username.setFont(font)
        self.username.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.username.setTextFormat(Qt.TextFormat.AutoText)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(240, 80, 671, 487))
        self.dashBoard = QWidget()
        self.dashBoard.setObjectName(u"dashBoard")
        self.welcome_label = QLabel(self.dashBoard)
        self.welcome_label.setObjectName(u"welcome_label")
        self.welcome_label.setGeometry(QRect(10, 10, 351, 41))
        self.welcome_label.setFont(font)
        self.welcome_label.setTextFormat(Qt.TextFormat.AutoText)
        self.horizontalLayoutWidget_5 = QWidget(self.dashBoard)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 70, 241, 31))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.quick_raw = QPushButton(self.horizontalLayoutWidget_5)
        self.quick_raw.setObjectName(u"quick_raw")

        self.horizontalLayout_10.addWidget(self.quick_raw)

        self.quick_stock = QPushButton(self.horizontalLayoutWidget_5)
        self.quick_stock.setObjectName(u"quick_stock")

        self.horizontalLayout_10.addWidget(self.quick_stock)

        self.quickie_add = QLabel(self.dashBoard)
        self.quickie_add.setObjectName(u"quickie_add")
        self.quickie_add.setGeometry(QRect(20, 50, 91, 16))
        self.quickie_add.setFont(font)
        self.quickie_add.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.quickie_add.setTextFormat(Qt.TextFormat.AutoText)
        self.task_abel = QLabel(self.dashBoard)
        self.task_abel.setObjectName(u"task_abel")
        self.task_abel.setGeometry(QRect(20, 110, 91, 16))
        self.task_abel.setFont(font)
        self.task_abel.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.task_abel.setTextFormat(Qt.TextFormat.AutoText)
        self.horizontalLayoutWidget_6 = QWidget(self.dashBoard)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 130, 501, 81))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.checkBox_5 = QCheckBox(self.horizontalLayoutWidget_6)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_20.addWidget(self.checkBox_5)

        self.checkBox_36 = QCheckBox(self.horizontalLayoutWidget_6)
        self.checkBox_36.setObjectName(u"checkBox_36")

        self.verticalLayout_20.addWidget(self.checkBox_36)

        self.checkBox_37 = QCheckBox(self.horizontalLayoutWidget_6)
        self.checkBox_37.setObjectName(u"checkBox_37")

        self.verticalLayout_20.addWidget(self.checkBox_37)


        self.horizontalLayout_11.addLayout(self.verticalLayout_20)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.checkBox_38 = QCheckBox(self.horizontalLayoutWidget_6)
        self.checkBox_38.setObjectName(u"checkBox_38")

        self.verticalLayout_21.addWidget(self.checkBox_38)

        self.checkBox_39 = QCheckBox(self.horizontalLayoutWidget_6)
        self.checkBox_39.setObjectName(u"checkBox_39")

        self.verticalLayout_21.addWidget(self.checkBox_39)

        self.checkBox_40 = QCheckBox(self.horizontalLayoutWidget_6)
        self.checkBox_40.setObjectName(u"checkBox_40")

        self.verticalLayout_21.addWidget(self.checkBox_40)


        self.horizontalLayout_11.addLayout(self.verticalLayout_21)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.checkBox_41 = QCheckBox(self.horizontalLayoutWidget_6)
        self.checkBox_41.setObjectName(u"checkBox_41")

        self.verticalLayout_22.addWidget(self.checkBox_41)

        self.checkBox_42 = QCheckBox(self.horizontalLayoutWidget_6)
        self.checkBox_42.setObjectName(u"checkBox_42")

        self.verticalLayout_22.addWidget(self.checkBox_42)

        self.checkBox_43 = QCheckBox(self.horizontalLayoutWidget_6)
        self.checkBox_43.setObjectName(u"checkBox_43")

        self.verticalLayout_22.addWidget(self.checkBox_43)


        self.horizontalLayout_11.addLayout(self.verticalLayout_22)

        self.label_22 = QLabel(self.dashBoard)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 220, 121, 16))
        self.label_22.setFont(font)
        self.label_22.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label_22.setTextFormat(Qt.TextFormat.AutoText)
        self.prod_table = QTableView(self.dashBoard)
        self.prod_table.setObjectName(u"prod_table")
        self.prod_table.setGeometry(QRect(10, 240, 501, 111))
        self.line_5 = QFrame(self.dashBoard)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(510, 10, 20, 371))
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_23 = QLabel(self.dashBoard)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(530, 20, 91, 16))
        self.label_23.setFont(font)
        self.label_23.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label_23.setTextFormat(Qt.TextFormat.AutoText)
        self.label = QLabel(self.dashBoard)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(530, 40, 131, 16))
        self.logout_button = QPushButton(self.dashBoard)
        self.logout_button.setObjectName(u"logout_button")
        self.logout_button.setGeometry(QRect(560, 330, 75, 24))
        self.stackedWidget.addWidget(self.dashBoard)
        self.production = QWidget()
        self.production.setObjectName(u"production")
        self.stackedWidget.addWidget(self.production)
        self.transac = QWidget()
        self.transac.setObjectName(u"transac")
        self.stackedWidget.addWidget(self.transac)
        self.help = QWidget()
        self.help.setObjectName(u"help")
        self.label_30 = QLabel(self.help)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(50, 110, 581, 211))
        font2 = QFont()
        font2.setFamilies([u"Poppins Light"])
        self.label_30.setFont(font2)
        self.label_31 = QLabel(self.help)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(50, 50, 381, 61))
        font3 = QFont()
        font3.setFamilies([u"Poppins ExtraBold"])
        font3.setPointSize(33)
        self.label_31.setFont(font3)
        self.stackedWidget.addWidget(self.help)
        self.maintenance = QWidget()
        self.maintenance.setObjectName(u"maintenance")
        self.maintenance_label = QLabel(self.maintenance)
        self.maintenance_label.setObjectName(u"maintenance_label")
        self.maintenance_label.setGeometry(QRect(90, 50, 361, 61))
        self.maintenance_label.setFont(font3)
        self.version_label = QLabel(self.maintenance)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setGeometry(QRect(90, 110, 381, 61))
        self.version_label.setFont(font2)
        self.update_button = QPushButton(self.maintenance)
        self.update_button.setObjectName(u"update_button")
        self.update_button.setGeometry(QRect(90, 180, 75, 24))
        self.backup_button = QPushButton(self.maintenance)
        self.backup_button.setObjectName(u"backup_button")
        self.backup_button.setGeometry(QRect(90, 250, 75, 24))
        self.restore_button = QPushButton(self.maintenance)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setGeometry(QRect(90, 280, 75, 24))
        self.stackedWidget.addWidget(self.maintenance)
        self.prod = QWidget()
        self.prod.setObjectName(u"prod")
        self.stackedWidget.addWidget(self.prod)
        self.sched = QWidget()
        self.sched.setObjectName(u"sched")
        self.stackedWidget.addWidget(self.sched)
        self.about = QWidget()
        self.about.setObjectName(u"about")
        self.label_2 = QLabel(self.about)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 80, 401, 61))
        self.label_2.setFont(font3)
        self.label_29 = QLabel(self.about)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(80, 130, 501, 161))
        self.label_29.setFont(font2)
        self.stackedWidget.addWidget(self.about)
        self.reports = QWidget()
        self.reports.setObjectName(u"reports")
        self.maintenance_label_2 = QLabel(self.reports)
        self.maintenance_label_2.setObjectName(u"maintenance_label_2")
        self.maintenance_label_2.setGeometry(QRect(80, 50, 361, 61))
        self.maintenance_label_2.setFont(font3)
        self.widget = QWidget(self.reports)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(80, 130, 361, 91))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.prod_report_btn = QPushButton(self.widget)
        self.prod_report_btn.setObjectName(u"prod_report_btn")

        self.verticalLayout_2.addWidget(self.prod_report_btn)

        self.inventory_report_btn = QPushButton(self.widget)
        self.inventory_report_btn.setObjectName(u"inventory_report_btn")

        self.verticalLayout_2.addWidget(self.inventory_report_btn)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stocks_report_btn = QPushButton(self.widget)
        self.stocks_report_btn.setObjectName(u"stocks_report_btn")

        self.verticalLayout_4.addWidget(self.stocks_report_btn)

        self.sales_report_btn = QPushButton(self.widget)
        self.sales_report_btn.setObjectName(u"sales_report_btn")

        self.verticalLayout_4.addWidget(self.sales_report_btn)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.stackedWidget.addWidget(self.reports)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(240, 70, 651, 20))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 100, 191, 331))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dash_button = QPushButton(self.widget1)
        self.dash_button.setObjectName(u"dash_button")
        self.dash_button.setFlat(True)

        self.verticalLayout.addWidget(self.dash_button)

        self.prod_button = QPushButton(self.widget1)
        self.prod_button.setObjectName(u"prod_button")
        self.prod_button.setFlat(True)

        self.verticalLayout.addWidget(self.prod_button)

        self.sched_button = QPushButton(self.widget1)
        self.sched_button.setObjectName(u"sched_button")
        self.sched_button.setFlat(True)

        self.verticalLayout.addWidget(self.sched_button)

        self.invent_button = QPushButton(self.widget1)
        self.invent_button.setObjectName(u"invent_button")
        self.invent_button.setFlat(True)

        self.verticalLayout.addWidget(self.invent_button)

        self.rep_button = QPushButton(self.widget1)
        self.rep_button.setObjectName(u"rep_button")
        self.rep_button.setFlat(True)

        self.verticalLayout.addWidget(self.rep_button)

        self.transac_button = QPushButton(self.widget1)
        self.transac_button.setObjectName(u"transac_button")
        self.transac_button.setFlat(True)

        self.verticalLayout.addWidget(self.transac_button)

        self.help_button = QPushButton(self.widget1)
        self.help_button.setObjectName(u"help_button")
        self.help_button.setFlat(True)

        self.verticalLayout.addWidget(self.help_button)

        self.about_button = QPushButton(self.widget1)
        self.about_button.setObjectName(u"about_button")
        self.about_button.setFlat(True)

        self.verticalLayout.addWidget(self.about_button)

        self.maintenance_button = QPushButton(self.widget1)
        self.maintenance_button.setObjectName(u"maintenance_button")
        self.maintenance_button.setFlat(True)

        self.verticalLayout.addWidget(self.maintenance_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_wannabe.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">Rexie Marie Bags</span></p></body></html>", None))
        self.menu_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:400;\">Menu Bar</span></p></body></html>", None))
        self.search_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:9pt; font-weight:400; color:#ffffff;\">Search</span></p></body></html>", None))
        self.search_bar.setText("")
        self.dashboard_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:400; color:#ffffff;\">Dashboard</span></p></body></html>", None))
        self.username.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:11pt; font-style:italic;\">Maris Pascual</span></p><p align=\"right\"><span style=\" font-size:9pt; font-style:italic; vertical-align:super;\">(Administrator)</span></p></body></html>", None))
        self.welcome_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-style:italic;\">WELCOME, Maris Pascual!</span></p></body></html>", None))
        self.quick_raw.setText(QCoreApplication.translate("MainWindow", u"Add Raw Material", None))
        self.quick_stock.setText(QCoreApplication.translate("MainWindow", u"Add Bag Product", None))
        self.quickie_add.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400; color:#ffffff;\">Quick Add</span></p></body></html>", None))
        self.task_abel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400; color:#ffffff;\">Tasks</span></p></body></html>", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Task 1", None))
        self.checkBox_36.setText(QCoreApplication.translate("MainWindow", u"Task 2", None))
        self.checkBox_37.setText(QCoreApplication.translate("MainWindow", u"Task 3", None))
        self.checkBox_38.setText(QCoreApplication.translate("MainWindow", u"Task 4", None))
        self.checkBox_39.setText(QCoreApplication.translate("MainWindow", u"Task 5", None))
        self.checkBox_40.setText(QCoreApplication.translate("MainWindow", u"Task 6", None))
        self.checkBox_41.setText(QCoreApplication.translate("MainWindow", u"Task 7", None))
        self.checkBox_42.setText(QCoreApplication.translate("MainWindow", u"Task 8", None))
        self.checkBox_43.setText(QCoreApplication.translate("MainWindow", u"Task 9", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400; color:#ffffff;\">Upcoming Deadlines</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:400; color:#ffffff;\">History</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:6pt;\">Maris Pascual Added a raw material</span></p></body></html>", None))
        self.logout_button.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Poppins Light'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">This program is the production management system for Rexie Maris Bag Enterprise.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">The program contains the following features as seen in the menu navigation bar in the left</span></p"
                        ">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:700;\">\u2022 Dashboard</span><span style=\" font-family:'Segoe UI';\"> is the overall view of the general production state</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:700;\">\u2022 Production Tracking </span><span style=\" font-family:'Segoe UI';\">contains the database of the current production status and the </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">corresponding buttons for its management</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI"
                        "'; font-weight:700;\">\u2022 Scheduling </span><span style=\" font-family:'Segoe UI';\">contains the deadlines and goals that are needed to be met</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:700;\">\u2022 Inventory Management </span><span style=\" font-family:'Segoe UI';\">contains the information about the raw materials for production</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:700;\">\u2022 Reports </span><span style=\" font-family:'Segoe UI';\">module contains the overview of the production process and inventory</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:700;\">\u2022 Transaction Histo"
                        "ry </span><span style=\" font-family:'Segoe UI';\">contains the records of data input in the system</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:700;\">\u2022 Help </span><span style=\" font-family:'Segoe UI';\">contains the general information about the system</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:700;\">\u2022 Maintenance </span><span style=\" font-family:'Segoe UI';\">contains the current system version and will serve as the portal for future updates.</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Help</p></body></html>", None))
        self.maintenance_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Maintenance</p></body></html>", None))
        self.version_label.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Poppins Light'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Current Version:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:24pt; font-weight:700;\">1.0.0</span></p></body></html>", None))
        self.update_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.backup_button.setText(QCoreApplication.translate("MainWindow", u"Backup", None))
        self.restore_button.setText(QCoreApplication.translate("MainWindow", u"Restore", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>About</p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Poppins Light'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">This application is the production management system for the Rexie Maris Bag Enterprise.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Thiswas developed by the students of Technological Institute of the Philippines Quezon City:"
                        "</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">\u2022 Amorato, Charlize</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">\u2022 Pasquil, Kristan Jay</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">\u2022 Roxas, Marx Gabriel</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">As a fulfillment for the requirements of the Software Engineering class under the Computer </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span st"
                        "yle=\" font-family:'Segoe UI';\">Science degree program curriculum.</span></p></body></html>", None))
        self.maintenance_label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Reports</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.prod_report_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.prod_report_btn.setText(QCoreApplication.translate("MainWindow", u"Generate Production Report", None))
#if QT_CONFIG(tooltip)
        self.inventory_report_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.inventory_report_btn.setText(QCoreApplication.translate("MainWindow", u"Generate Inventory Report", None))
#if QT_CONFIG(tooltip)
        self.stocks_report_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.stocks_report_btn.setText(QCoreApplication.translate("MainWindow", u"Generate Stocks Report", None))
#if QT_CONFIG(tooltip)
        self.sales_report_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sales_report_btn.setText(QCoreApplication.translate("MainWindow", u"Generate Sales Report", None))
        self.dash_button.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.prod_button.setText(QCoreApplication.translate("MainWindow", u"Production Tracking", None))
        self.sched_button.setText(QCoreApplication.translate("MainWindow", u"Scheduling", None))
        self.invent_button.setText(QCoreApplication.translate("MainWindow", u"Inventory Management", None))
        self.rep_button.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.transac_button.setText(QCoreApplication.translate("MainWindow", u"Transaction History", None))
        self.help_button.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.about_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.maintenance_button.setText(QCoreApplication.translate("MainWindow", u"Maintenance", None))
    # retranslateUi

